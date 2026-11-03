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
OUTPUT_DIR = ROOT_DIR / "docs" / "projects"
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
        formatted_content = format_readme_content(repo_name, html_url, existing_content)
        if existing_content != formatted_content:
            target_path.write_text(formatted_content, encoding="utf-8")
            print(f"Updated formatting in: {target_path}")


def update_mkdocs_yml(projects_output_dir, mkdocs_path):
    """Update the Projects section in mkdocs.yml, including custom rule subfolders."""
    projects_output_dir = Path(projects_output_dir)
    mkdocs_path = Path(mkdocs_path)

    if not mkdocs_path.exists():
        print(f"Warning: mkdocs.yml not found at {mkdocs_path}")
        return

    project_entries = []

    for md_file in projects_output_dir.glob("*.md"):
        project_title = format_title(md_file.stem)
        project_entries.append(
            (project_title, f"  - {project_title}: projects/{md_file.name}")
        )

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
    projects_block = "\n".join(entry for _, entry in project_entries) + "\n"

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

        update_mkdocs_yml(OUTPUT_DIR, MKDOCS_PATH)
    finally:
        remove_dir(TEMP_DIR)


if __name__ == "__main__":
    main()
