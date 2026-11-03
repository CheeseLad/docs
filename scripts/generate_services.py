import os
import re
import shutil
import stat
import subprocess
from pathlib import Path
import yaml
from dotenv import load_dotenv
from google import genai
from google.genai import types
from groq import Groq

# Load environment variables from .env file
load_dotenv()

ROOT_DIR = Path(__file__).resolve().parent.parent
TEMP_DIR = Path(".\\tmp")
AI_TYPE = os.getenv("AI_TYPE", "groq").lower()  # "gemini" or "groq"
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

SERVICE_DEVICES = {
    "homelab": [
        {
            "title": "homelab",
            "prompt_title": "home server",
            "repo": "https://github.com/CheeseLad/homelab",
        }
    ],
    "vps": [
        {
            "title": "vps",
            "prompt_title": "virtual private server",
            "repo": "https://github.com/CheeseLad/vps",
        }
    ],
}

IGNORED_ACCESS_NOTES_SERVICES = {
    "collegeguide-redis",
    "wings",
    "mysql-database",
    "better-file-search-postgres",
    "database",
}

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
}

NOTES_REPLACEMENTS = {
    "[http://cheeselab:1313](http://cheeselab:1313) (Local Network Only)": "[https://collegeguide-blog.jakefarrell.ie](https://collegeguide-blog.jakefarrell.ie) (Publicly Accessible)",
    "[http://cheeselab:802](http://cheeselab:802) (Local Network Only)": "[https://panel.cablenetwork.xyz](https://panel.cablenetwork.xyz) (Publicly Accessible)",
    "http://cheeselab:9443": "https://cheeselab:9443",
    "[http://cheeselab:6022](http://cheeselab:6022) (Local Network Only)": "[https://cablenetwork.jakefarrell.ie](https://cablenetwork.jakefarrell.ie) (Publicly Accessible)",
    "[http://cheeselab:3020](http://cheeselab:3020) (Local Network Only)": "[https://dcumps.jakefarrell.ie](https://dcumps.jakefarrell.ie) (Publicly Accessible)",
    "[http://cheeselab:3021](http://cheeselab:3021) (Local Network Only)": "[https://pizzashop.jakefarrell.ie](https://pizzashop.jakefarrell.ie) (Publicly Accessible)",
    "[http://cheeselab:3003](http://cheeselab:3003) (Local Network Only)": "[https://status.jakefarrell.ie](https://status.jakefarrell.ie) (Publicly Accessible)",
    "[http://cheeselab:3022](http://cheeselab:3022) (Local Network Only)": "[https://nyancat.jakefarrell.ie](https://nyancat.jakefarrell.ie) (Publicly Accessible)",
    "[http://cheeselab:3023](http://cheeselab:3023) (Local Network Only)": "[https://tcvapp.jakefarrell.ie](https://tcvapp.jakefarrell.ie) (Publicly Accessible)",
    "[http://cheeselab:3018](http://cheeselab:3018) (Local Network Only)": "[https://csc1047-practical.jakefarrell.ie](https://csc1047-practical.jakefarrell.ie) (Publicly Accessible)",
    "[http://cheeselab:3024](http://cheeselab:3024) (Local Network Only)": "[https://betterfilesearch.jakefarrell.ie](https://betterfilesearch.jakefarrell.ie) (Publicly Accessible)",
    "[http://cheeselab:3025](http://cheeselab:3025) (Local Network Only)": "[https://betterfilesearch-api.jakefarrell.ie](https://betterfilesearch-api.jakefarrell.ie) (Publicly Accessible)",
}


def generate_prompt(device_title, service_name):
    return (
        f"Write a maximum of 4 sentences about the {device_title} service {service_name}, "
        "look up the project's README for more information. Give a brief description of the "
        "service, its purpose, and any useful features. Make it not too formal."
    )


def get_gemini_response(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in the environment or .env file.")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())],
        ),
    )
    return response.text.strip()


def get_groq_response(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in the environment or .env file.")

    client = Groq(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=GROQ_MODEL,
        max_tokens=1000,
    )
    return chat_completion.choices[0].message.content.strip()


def get_ai_response(prompt):
    if AI_TYPE == "gemini":
        return get_gemini_response(prompt)
    elif AI_TYPE == "groq":
        return get_groq_response(prompt)
    else:
        raise ValueError(f"Unsupported AI_TYPE '{AI_TYPE}'. Expected 'gemini' or 'groq'.")


def format_title(service_folder_name):
    title_name = service_folder_name.replace("-", " ").title()
    for target, replacement in TITLE_REPLACEMENTS.items():
        title_name = title_name.replace(target, replacement)
    return title_name


def extract_ports(compose_path):
    with open(compose_path, "r", encoding="utf-8") as f:
        compose_data = yaml.safe_load(f) or {}

    ports_info = []
    try:
        services = compose_data.get("services", {})
        for service_name, service_data in services.items():
            ports = service_data.get("ports", [])
            if ports:
                first_port = str(ports[0]).split(":")[0].split("/")[0]
                ports_info.append((service_name, first_port))
    except Exception as e:
        print(f"Warning: Could not extract ports from {compose_path}: {e}")
    return ports_info


def extract_traefik_domains(compose_data):
    """Extract public domains from Traefik labels."""
    traefik_domains = {}
    services = compose_data.get("services", {})

    for service_name, service_data in services.items():
        labels = service_data.get("labels", [])
        if not labels:
            continue

        domains = []
        if isinstance(labels, list):
            for label in labels:
                if isinstance(label, str):
                    domains.extend(re.findall(r"Host\(`([^`]+)`\)", label))
                elif isinstance(label, dict):
                    for v in label.values():
                        if isinstance(v, str):
                            domains.extend(re.findall(r"Host\(`([^`]+)`\)", v))
        elif isinstance(labels, dict):
            for v in labels.values():
                if isinstance(v, str):
                    domains.extend(re.findall(r"Host\(`([^`]+)`\)", v))

        if domains:
            traefik_domains[service_name] = domains

    return traefik_domains


def extract_public_env_urls(compose_content, compose_data):
    """Extract public URLs or bare domains from service environment variables."""
    public_env_urls = {}
    try:
        services = compose_data.get("services", {})
        for service_name, service_data in services.items():
            envs = service_data.get("environment", [])
            env_values = []
            if isinstance(envs, list):
                env_values = [e for e in envs if isinstance(e, str)]
            elif isinstance(envs, dict):
                env_values = [v for v in envs.values() if isinstance(v, str)]

            for val in env_values:
                url_match = re.search(r"https?://[\w\-\.]+\.[a-z]{2,}", val)
                if url_match and service_name not in public_env_urls:
                    public_env_urls[service_name] = url_match.group(0)
                if service_name not in public_env_urls:
                    for part in re.split(r"[=, ]", val):
                        if re.match(r"[\w\-\.]+\.[a-z]{2,}$", part) and not part.startswith("http"):
                            public_env_urls[service_name] = f"https://{part}"
                            break

            if service_name not in public_env_urls:
                service_start = compose_content.find(f"{service_name}:")
                if service_start != -1:
                    env_start = compose_content.find("environment:", service_start)
                    if env_start != -1:
                        next_section = compose_content.find("\n  ", env_start + 20)
                        if next_section == -1:
                            next_section = len(compose_content)
                        env_section = compose_content[env_start:next_section]
                        url_matches = re.findall(r"https?://[\w\-\.]+\.[a-z]{2,}", env_section)
                        if url_matches:
                            public_env_urls[service_name] = url_matches[0]
    except Exception as e:
        print(f"Warning: Could not extract public env URLs: {e}")

    return public_env_urls


def build_notes(device_title, service_folder_name, compose_content, compose_data, ports_info):
    if "-disabled" in service_folder_name:
        return "None"

    api_url_match = re.search(r"(https?://[\w\-]+-api\.jakefarrell\.ie)", compose_content)
    backend_url = api_url_match.group(1) if api_url_match else None
    frontend_url = backend_url.replace("-api.jakefarrell.ie", ".jakefarrell.ie") if backend_url else None

    public_env_urls = extract_public_env_urls(compose_content, compose_data)
    traefik_domains = extract_traefik_domains(compose_data) if device_title == "vps" else {}

    notes_lines = []
    services = compose_data.get("services", {})
    ports_by_service = dict(ports_info)

    for service_name in services.keys():
        if service_name in IGNORED_ACCESS_NOTES_SERVICES:
            continue

        if service_name in traefik_domains:
            for domain in traefik_domains[service_name]:
                url = f"https://{domain}"
                notes_lines.append(
                    f"- Access `{service_name}` at [{url}]({url}) (Publicly Accessible via Traefik)"
                )
            continue

        if backend_url and frontend_url and service_name in ports_by_service:
            if "frontend" in service_name:
                notes_lines.append(
                    f"- Access `{service_name}` at [{frontend_url}]({frontend_url}) (Publicly Accessible)"
                )
                continue
            if "backend" in service_name:
                notes_lines.append(
                    f"- Access `{service_name}` at [{backend_url}]({backend_url}) (Publicly Accessible)"
                )
                continue

        if service_name in public_env_urls and service_name in ports_by_service:
            url = public_env_urls[service_name]
            notes_lines.append(
                f"- Access `{service_name}` at [{url}]({url}) (Publicly Accessible)"
            )
            continue

        if service_name in ports_by_service:
            port = ports_by_service[service_name]
            notes_lines.append(
                f"- Access `{service_name}` at [http://cheeselab:{port}](http://cheeselab:{port}) (Local Network Only)"
            )

    notes = "\n".join(notes_lines) if notes_lines else "None"
    for target, replacement in NOTES_REPLACEMENTS.items():
        notes = notes.replace(target, replacement)

    return notes


def generate_markdown(device, service_folder_name, compose_content, ports_info, output_dir):
    compose_data = yaml.safe_load(compose_content) or {}
    services = compose_data.get("services", {})
    image = services.get(service_folder_name, {}).get("image", service_folder_name)

    title_name = format_title(service_folder_name)
    notes = build_notes(device["title"], service_folder_name, compose_content, compose_data, ports_info)

    print(f"Generating description for: {title_name}")
    existing_md_path = output_dir / f"{service_folder_name}.md"
    description = None

    if existing_md_path.exists():
        existing_content = existing_md_path.read_text(encoding="utf-8")
        desc_match = re.search(
            r"## Description\s+([\s\S]+?)\s+## Docker Compose File", existing_content
        )
        if desc_match:
            description = desc_match.group(1).strip()
            print(f"Using existing description for: {title_name}")

    if not description:
        prompt = generate_prompt(device["prompt_title"], f"{title_name} ({image})")
        description = get_ai_response(prompt)

    md_content = f"""# {title_name}
    
    

## Description

{description}

## Docker Compose File

```yaml
{compose_content}
```

## Notes

{notes}"""

    output_path = output_dir / f"{service_folder_name}.md"
    output_path.write_text(md_content, encoding="utf-8")
    print(f"Generated: {output_path}")


def process_services_dir(device, services_dir, output_dir):
    services_dir = Path(services_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not services_dir.exists():
        print(f"Services directory not found: {services_dir}")
        return

    existing_service_folders = {
        service_folder.name
        for service_folder in services_dir.iterdir()
        if service_folder.is_dir() and "-disabled" not in service_folder.name
    }

    for service_folder in sorted(services_dir.iterdir()):
        if not service_folder.is_dir() or "-disabled" in service_folder.name:
            continue

        compose_path = service_folder / "docker-compose.yml"
        if compose_path.exists():
            compose_content = compose_path.read_text(encoding="utf-8")
            ports_info = extract_ports(compose_path)
            generate_markdown(device, service_folder.name, compose_content, ports_info, output_dir)

    for md_file in output_dir.glob("*.md"):
        if md_file.stem not in existing_service_folders:
            md_file.unlink()
            print(f"Deleted orphaned markdown: {md_file}")


def _handle_remove_readonly(func, path, exc):
    """Clear the read-only bit (e.g. on Windows .git pack files) and retry removal."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def remove_dir(path):
    path = Path(path)
    if path.exists():
        shutil.rmtree(path, onexc=_handle_remove_readonly)


def clone_and_generate(device):
    repo_url = device["repo"]
    device_title = device["title"]
    repo_path = TEMP_DIR / device_title
    services_path = repo_path / "services"
    output_dir = ROOT_DIR / "docs" / device_title / "services"

    remove_dir(repo_path)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    try:
        print(f"Cloning {repo_url} into {repo_path}...")
        subprocess.check_call(["git", "clone", repo_url, str(repo_path)])
        process_services_dir(device, services_path, output_dir)
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository {repo_url}: {e}")
    finally:
        if repo_path.exists():
            print(f"Cleaning up {repo_path}...")
            remove_dir(repo_path)


def main():
    remove_dir(TEMP_DIR)
    try:
        for device_list in SERVICE_DEVICES.values():
            for device in device_list:
                clone_and_generate(device)
    finally:
        remove_dir(TEMP_DIR)


if __name__ == "__main__":
    main()
