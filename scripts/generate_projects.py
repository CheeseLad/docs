import json
import os
import re
import shutil
import stat
import subprocess
import urllib.error
import urllib.request
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ROOT_DIR = Path(__file__).resolve().parent.parent
TEMP_DIR = Path(".\\tmp")
DOCS_DIR = ROOT_DIR / "docs"
ASSETS_DIR = DOCS_DIR / "assets"
OUTPUT_DIR = DOCS_DIR / "projects"
MKDOCS_PATH = ROOT_DIR / "mkdocs.yml"

REPO_ACCOUNT_URL = "https://github.com/CheeseLad"

IGNORE_FORKS = True

EXCLUDED_REPOS = {
    "CheeseLad",
    "docs",
    "homelab",
    "vps",
    "advent-of-code",
    "amazon-price-tracker",
    "brainrot-dashboard",
    "cat-bot",
    "cheeseconvert",
    "hackerrank",
    "hackireland-team25",
    "hangman-py",
    "hello-world",
    "Kattis",
    "LeetCode",
    "pixelbros",
    "python-projects",
    "pythonfiles",
    "rsa-checker",
    "shell-scripts",
    "wisetek-scrape"

}

PRESERVED_MD_FILES = {
    "email-system",
    "info",
}

CUSTOM_FOLDER_RULES = [
    {
        "folder": "college",
        "prefixes": ["ca", "csc"],
        "include": ["project-euler"],
        "exclude": ["cablenetwork-website", "cat-bot"],
    },
    {
        "folder": "redbrick",
        "prefixes": ["redbrick"],
        "include": ["minute-redactor"]
    },
    {
        "folder": "mps",
        "prefixes": ["mps"],
        "include": ["thecollegeview-app"],
    },
    {
        "folder": "fotosoc",
        "prefixes": ["fotosoc"],
    },
    {
        "folder": "terraria",
        "include": ["boxinator", "BoxinatorTerraria", "technobladepainting", "TysYoyoRedux144", "YoyoMania"],
    },
    {
        "folder": "unturned",
        "include": ["cablenetwork-website", "testplugin", "uconomy-mysql-search", "unturned-permission-generator"],
    }
]

TITLE_REPLACEMENTS = {
    "Ca298": "CA298",
    "Cablenetwork": "Cable Network",
    "Collegeguide": "CollegeGuide",
    "Mysql": "MySQL",
    "Ddclient": "DDClient",
    "Reactexam": "React Exam",
    "Universitysystem": "University System",
    "Macos": "macOS",
    "Clubsandsocs": "Clubs & Socs",
    "Api": "API",
    "Dcu": "DCU",
    "CA298 Pizzashop": "CA298 PizzaShop",
    "DCUmps": "DCUMPS",
    "Nyancat": "Nyan Cat",
    "Tcvapp": "The College View App",
    "DCUfotosoc Generator": "DCU Fotosoc Newsletter Generator",
    "Csc1047": "CSC1047",
    "Thecollegeview": "The College View",
    "DCUfotosoc": "DCU Fotosoc",
    "Database": "MySQL Database",
    "DCUclubsandsocs": "DCU Clubs & Socs",
    "MySQL MySQL": "MySQL",
    "Mps": "MPS",
    "mps": "MPS",
}


def format_title(name):
    title_name = name.replace("-", " ").replace("_", " ").title()
    for target, replacement in TITLE_REPLACEMENTS.items():
        title_name = title_name.replace(target, replacement)
    return title_name


def get_project_subfolder(repo_name):
    """Return the target subfolder name for a repo based on CUSTOM_FOLDER_RULES, or None."""
    repo_lower = repo_name.lower()
    for rule in CUSTOM_FOLDER_RULES:
        folder = rule.get("folder")
        if not folder:
            continue
        excluded = {r.lower() for r in rule.get("exclude", [])}
        if repo_lower in excluded:
            continue
        included = {
            r.lower() for r in (*rule.get("include", []), *rule.get("repos", []))
        }
        prefixes = tuple(p.lower() for p in rule.get("prefixes", []))
        if repo_lower in included or (prefixes and repo_lower.startswith(prefixes)):
            return folder
    return None


def _handle_remove_readonly(func, path, exc):
    """Clear the read-only bit (e.g. on Windows .git pack files) and retry removal."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def remove_dir(path):
    path = Path(path)
    if path.exists():
        shutil.rmtree(path, onexc=_handle_remove_readonly)


def get_account_username(account_url):
    return account_url.rstrip("/").split("/")[-1]


def fetch_public_repos(account_url):
    """Fetch all public repositories for the given GitHub account URL."""
    username = get_account_username(account_url)
    excluded_lower = {repo.lower() for repo in EXCLUDED_REPOS}
    repos = []
    page = 1

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "docs-project-generator",
    }
    github_token = os.getenv("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"

    while True:
        api_url = (
            f"https://api.github.com/users/{username}/repos"
            f"?type=public&per_page=100&page={page}"
        )
        req = urllib.request.Request(api_url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                page_repos = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            print(f"Error fetching repositories from {api_url}: {e}")
            break
        except urllib.error.URLError as e:
            print(f"Network error fetching repositories from {api_url}: {e}")
            break

        if not page_repos:
            break

        for repo in page_repos:
            repo_name = repo.get("name", "")
            if repo.get("private", False):
                continue
            if IGNORE_FORKS and repo.get("fork", False):
                print(f"Skipping forked repo: {repo_name}")
                continue
            if repo_name in EXCLUDED_REPOS or repo_name.lower() in excluded_lower:
                print(f"Skipping excluded repo: {repo_name}")
                continue
            repos.append(
                {
                    "name": repo_name,
                    "clone_url": repo.get("clone_url")
                    or f"https://github.com/{username}/{repo_name}.git",
                    "html_url": repo.get("html_url")
                    or f"https://github.com/{username}/{repo_name}",
                }
            )

        if len(page_repos) < 100:
            break
        page += 1

    repos.sort(key=lambda r: r["name"].lower())
    return repos


def find_readme(repo_dir):
    """Find the README file in the cloned repository (case-insensitive)."""
    repo_dir = Path(repo_dir)
    for item in repo_dir.iterdir():
        if item.is_file() and item.name.lower() in {"readme.md", "readme.markdown", "readme"}:
            return item
    return None


def format_readme_content(repo_name, html_url, readme_content):
    """Ensure the first line has a # heading and add the GitHub Repository Link under it."""
    readme_content = readme_content.strip()
    lines = readme_content.splitlines()
    link_line = f"*[GitHub Repository Link]({html_url})*"
    if not lines:
        return f"# {repo_name}\n\n{link_line}\n"

    if "#" in lines[0]:
        heading_line = lines[0].strip()
        rest_lines = lines[1:]
    else:
        heading_line = f"# {repo_name}"
        rest_lines = lines

    while rest_lines and not rest_lines[0].strip():
        rest_lines.pop(0)
    if rest_lines and rest_lines[0].strip().strip("*").startswith("[GitHub Repository Link]("):
        rest_lines.pop(0)
        while rest_lines and not rest_lines[0].strip():
            rest_lines.pop(0)

    rest_content = "\n".join(rest_lines).strip()

    if rest_content:
        return f"{heading_line}\n\n{link_line}\n\n{rest_content}\n"
    return f"{heading_line}\n\n{link_line}\n"


def copy_and_rewrite_repo_assets(readme_content, repo_path, target_dir):
    """Copy repo files referenced by relative links in readme_content to docs/assets/projects/<repo_name> and rewrite links."""
    repo_path = Path(repo_path)
    target_dir = Path(target_dir)
    repo_name = repo_path.name

    def resolve_and_copy(raw_url):
        url = raw_url.strip()
        if not url or url.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#")):
            return raw_url

        # Split optional markdown link title, e.g. 'path/to/img.png "Title"'
        title_part = ""
        title_match = re.match(r'^([^\s]+)(\s+["\'].*["\'])$', url)
        if title_match:
            url = title_match.group(1)
            title_part = title_match.group(2)

        # Separate query/fragment from path
        suffix = ""
        for sep in ("?", "#"):
            if sep in url:
                idx = url.index(sep)
                suffix = url[idx:]
                url = url[:idx]
                break

        clean_rel = url.lstrip("./").lstrip("/")
        if not clean_rel or clean_rel.startswith("assets/") or "/assets/" in url:
            return raw_url

        source_file = (repo_path / clean_rel).resolve()
        try:
            source_file.relative_to(repo_path.resolve())
        except ValueError:
            return raw_url

        if not source_file.is_file():
            return raw_url

        asset_dest = ASSETS_DIR / "projects" / repo_name / clean_rel
        asset_dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, asset_dest)
        print(f"Copied asset: {source_file} -> {asset_dest}")

        rel_link = Path(os.path.relpath(asset_dest, target_dir)).as_posix()
        return f"{rel_link}{suffix}{title_part}"

    # Rewrite Markdown links/images: ![alt](url) and [text](url)
    md_link_pattern = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")
    readme_content = md_link_pattern.sub(
        lambda m: f"{m.group(1)}{resolve_and_copy(m.group(2))}{m.group(3)}",
        readme_content,
    )

    # Rewrite HTML src/href attributes: src="url" or href="url"
    html_attr_pattern = re.compile(r'((?:src|href)=["\'])([^"\']+)(["\'])')
    readme_content = html_attr_pattern.sub(
        lambda m: f"{m.group(1)}{resolve_and_copy(m.group(2))}{m.group(3)}",
        readme_content,
    )

    return readme_content


def clone_and_generate_project(repo, output_dir):
    """Clone a repository and write its README as a markdown file in output_dir (or rule subfolder)."""
    repo_name = repo["name"]
    clone_url = repo["clone_url"]
    html_url = repo.get("html_url") or f"{REPO_ACCOUNT_URL.rstrip('/')}/{repo_name}"
    repo_path = TEMP_DIR / repo_name
    output_dir = Path(output_dir)

    subfolder = get_project_subfolder(repo_name)
    target_dir = output_dir / subfolder if subfolder else output_dir
    target_dir.mkdir(parents=True, exist_ok=True)

    remove_dir(repo_path)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    try:
        print(f"Cloning {clone_url} into {repo_path}...")
        subprocess.check_call(["git", "clone", "--depth", "1", clone_url, str(repo_path)])

        readme_path = find_readme(repo_path)
        if not readme_path:
            print(f"Warning: No README found in {repo_name}, skipping...")
            return None

        readme_content = readme_path.read_text(encoding="utf-8", errors="replace").strip()
        if not readme_content:
            print(f"Warning: Empty README in {repo_name}, skipping...")
            return None

        readme_content = copy_and_rewrite_repo_assets(readme_content, repo_path, target_dir)
        formatted_content = format_readme_content(repo_name, html_url, readme_content)
        output_path = target_dir / f"{repo_name}.md"
        output_path.write_text(formatted_content, encoding="utf-8")
        print(f"Generated: {output_path}")
        return output_path.relative_to(output_dir)
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository {clone_url}: {e}")
        return None
    finally:
        if repo_path.exists():
            print(f"Cleaning up {repo_path}...")
            remove_dir(repo_path)


def has_missing_relative_assets(markdown_content, target_dir):
    """Return True if markdown_content has relative file links that do not exist under target_dir."""
    target_dir = Path(target_dir)
    md_links = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", markdown_content)
    html_links = re.findall(r'(?:src|href)=["\']([^"\']+)["\']', markdown_content)

    for raw_url in (*md_links, *html_links):
        url = raw_url.strip().split()[0] if raw_url.strip() else ""
        if not url or url.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#")):
            continue
        for sep in ("?", "#"):
            if sep in url:
                url = url[: url.index(sep)]
        if not url:
            continue
        resolved = (target_dir / url).resolve()
        if not resolved.exists():
            return True
    return False


def apply_folder_rules(output_dir):
    """Move any existing markdown files in output_dir into their target folders and remove excluded ones."""
    output_dir = Path(output_dir)
    if not output_dir.exists():
        return

    excluded_lower = {repo.lower() for repo in EXCLUDED_REPOS}

    for md_file in list(output_dir.rglob("*.md")):
        if md_file.stem in PRESERVED_MD_FILES:
            continue
        if md_file.stem in EXCLUDED_REPOS or md_file.stem.lower() in excluded_lower:
            md_file.unlink()
            print(f"Deleted excluded project markdown: {md_file}")
            continue
        subfolder = get_project_subfolder(md_file.stem)
        target_dir = output_dir / subfolder if subfolder else output_dir
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / md_file.name
        if md_file.resolve() != target_path.resolve():
            shutil.move(str(md_file), str(target_path))
            print(f"Moved {md_file} -> {target_path}")

        repo_name = target_path.stem
        html_url = f"{REPO_ACCOUNT_URL.rstrip('/')}/{repo_name}"
        existing_content = target_path.read_text(encoding="utf-8", errors="replace")

        if has_missing_relative_assets(existing_content, target_dir):
            repo_path = TEMP_DIR / repo_name
            clone_url = f"{html_url}.git"
            remove_dir(repo_path)
            TEMP_DIR.mkdir(parents=True, exist_ok=True)
            try:
                print(f"Cloning {clone_url} to resolve missing assets for {repo_name}...")
                subprocess.check_call(
                    ["git", "clone", "--depth", "1", clone_url, str(repo_path)]
                )
                existing_content = copy_and_rewrite_repo_assets(
                    existing_content, repo_path, target_dir
                )
            except subprocess.CalledProcessError as e:
                print(f"Error cloning repository {clone_url} for assets: {e}")
            finally:
                if repo_path.exists():
                    remove_dir(repo_path)

        formatted_content = format_readme_content(repo_name, html_url, existing_content)
        if target_path.read_text(encoding="utf-8", errors="replace") != formatted_content:
            target_path.write_text(formatted_content, encoding="utf-8")
            print(f"Updated formatting in: {target_path}")


def update_info_md(projects_output_dir, info_md_path):
    """Create or update docs/projects/info.md with ## All for ungrouped projects and sections for each subfolder."""
    projects_output_dir = Path(projects_output_dir)
    info_md_path = Path(info_md_path)

    default_intro = (
        "# Projects Information\n\n"
        "## Introduction\n\n"
        "This is a collection of various personal, college, and society projects that I have worked on."
    )

    intro_section = default_intro
    if info_md_path.exists():
        existing_content = info_md_path.read_text(encoding="utf-8")
        intro_match = re.match(r"([\s\S]*?)(?=\r?\n\r?\n## (?:All\b))", existing_content)
        if intro_match and intro_match.group(1).strip():
            intro_section = intro_match.group(1).strip()

    ungrouped_entries = []
    for md_file in projects_output_dir.glob("*.md"):
        if md_file.stem == "info":
            continue
        project_title = format_title(md_file.stem)
        ungrouped_entries.append((project_title, f"- [{project_title}](./{md_file.name})"))
    ungrouped_entries.sort(key=lambda item: item[0].lower())

    sections = []
    all_block = "\n".join(entry for _, entry in ungrouped_entries) if ungrouped_entries else "None"
    sections.append(f"## All\n\n{all_block}")

    folder_sections = []
    for subdir in sorted(p for p in projects_output_dir.iterdir() if p.is_dir()):
        sub_entries = []
        for md_file in subdir.glob("*.md"):
            project_title = format_title(md_file.stem)
            sub_entries.append(
                (project_title, f"- [{project_title}](./{subdir.name}/{md_file.name})")
            )
        if sub_entries:
            sub_entries.sort(key=lambda item: item[0].lower())
            folder_title = format_title(subdir.name)
            sub_block = "\n".join(entry for _, entry in sub_entries)
            folder_sections.append((folder_title, f"## {folder_title}\n\n{sub_block}"))

    folder_sections.sort(key=lambda item: item[0].lower())
    sections.extend(block for _, block in folder_sections)

    updated_content = f"{intro_section}\n\n" + "\n\n".join(sections) + "\n"
    info_md_path.write_text(updated_content, encoding="utf-8")
    print(f"Updated projects info in: {info_md_path}")


def update_mkdocs_yml(projects_output_dir, mkdocs_path):
    """Update the Projects section in mkdocs.yml, including custom rule subfolders."""
    projects_output_dir = Path(projects_output_dir)
    mkdocs_path = Path(mkdocs_path)

    if not mkdocs_path.exists():
        print(f"Warning: mkdocs.yml not found at {mkdocs_path}")
        return

    project_entries = []

    ungrouped_entries = []
    for md_file in projects_output_dir.glob("*.md"):
        if md_file.stem == "info":
            continue
        project_title = format_title(md_file.stem)
        ungrouped_entries.append(
            (project_title, f"      - {project_title}: projects/{md_file.name}")
        )
    if ungrouped_entries:
        ungrouped_entries.sort(key=lambda item: item[0].lower())
        all_block = "  - All:\n" + "\n".join(
            entry for _, entry in ungrouped_entries
        )
        project_entries.append(("All", all_block))

    for subdir in sorted(p for p in projects_output_dir.iterdir() if p.is_dir()):
        sub_entries = []
        for md_file in subdir.glob("*.md"):
            project_title = format_title(md_file.stem)
            sub_entries.append(
                (project_title, f"      - {project_title}: projects/{subdir.name}/{md_file.name}")
            )
        if sub_entries:
            sub_entries.sort(key=lambda item: item[0].lower())
            folder_title = format_title(subdir.name)
            folder_block = f"  - {folder_title}:\n" + "\n".join(
                entry for _, entry in sub_entries
            )
            project_entries.append((folder_title, folder_block))

    project_entries.sort(key=lambda item: item[0].lower())
    nav_lines = []
    if (projects_output_dir / "info.md").exists():
        nav_lines.append("  - Projects Information: projects/info.md")
    nav_lines.extend(entry for _, entry in project_entries)
    projects_block = "\n".join(nav_lines) + "\n"

    mkdocs_content = mkdocs_path.read_text(encoding="utf-8")

    pattern = (
        r"(^- Projects:\r?\n)"
        r"(?:[ ]{2,}- .*(?:\r?\n|$))*"
    )

    if not re.search(pattern, mkdocs_content, flags=re.MULTILINE):
        print(f"Warning: Could not find '- Projects:' section in {mkdocs_path}")
        return

    updated_content = re.sub(
        pattern,
        lambda m: f"{m.group(1)}{projects_block}",
        mkdocs_content,
        count=1,
        flags=re.MULTILINE,
    )
    mkdocs_path.write_text(updated_content, encoding="utf-8")
    print(f"Updated Projects in: {mkdocs_path}")


def main():
    remove_dir(TEMP_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    try:
        apply_folder_rules(OUTPUT_DIR)
        repos = fetch_public_repos(REPO_ACCOUNT_URL)
        print(f"Found {len(repos)} public repositories to process.")

        active_rel_paths = {Path(f"{stem}.md") for stem in PRESERVED_MD_FILES}
        for repo in repos:
            rel_path = clone_and_generate_project(repo, OUTPUT_DIR)
            if rel_path:
                active_rel_paths.add(rel_path)

        if repos:
            for md_file in OUTPUT_DIR.rglob("*.md"):
                if md_file.relative_to(OUTPUT_DIR) not in active_rel_paths:
                    md_file.unlink()
                    print(f"Deleted orphaned project markdown: {md_file}")

        info_md_path = OUTPUT_DIR / "info.md"
        update_info_md(OUTPUT_DIR, info_md_path)
        update_mkdocs_yml(OUTPUT_DIR, MKDOCS_PATH)
    finally:
        remove_dir(TEMP_DIR)


if __name__ == "__main__":
    main()
