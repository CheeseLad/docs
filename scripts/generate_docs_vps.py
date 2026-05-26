import yaml
import re
import os
import tempfile
import subprocess
import shutil
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

system_prompt = {
    "role": "system",
    "content": "Your job is to write a maximum of 4 sentences about the vps / virtual private server service name provided by the user. Give a brief description of the service, its purpose, and any useful features. Not too formal.",
}

def main(services_dir, output_dir):
    services_dir = Path(services_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for service_folder in services_dir.iterdir():
        if service_folder.is_dir():
            # Skip folders with '-disabled' in the name
            if "-disabled" in service_folder.name:
                continue
            compose_path = service_folder / "docker-compose.yml"
            if compose_path.exists():
                folder_name = service_folder.name
                with open(compose_path, "r") as f:
                    compose_content = f.read()
                ports_info = extract_ports(compose_path)
                generate_markdown(folder_name, compose_content, ports_info, output_dir)

def clone_and_run(repo_url, output_dir):
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp(prefix="repo_")
    repo_path = Path(temp_dir) / "repo"
    services_path = repo_path / "services"

    try:
        print(f"Cloning into: {repo_path}")

        # Clone the repository
        subprocess.check_call(["git", "clone", repo_url, str(repo_path)])


        main(services_path, output_dir)

        print("Command finished successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

    finally:
        # Cleanup
        print(f"Deleting temporary repo: {temp_dir}")
        shutil.rmtree(temp_dir, ignore_errors=True)

# chat history can be optional due to a user either deleting their chat history or starting a new one
def get_chatbot_response(message):

    chatbot_message = [system_prompt]

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    chatbot_message.append({"role": "user", "content": message})

    # limiting max tokens to 1000
    chat_completion = client.chat.completions.create(
        messages=chatbot_message,
        model="llama-3.3-70b-versatile",
        max_tokens=1000,
    )

    chatbot_message.append(
        {
            "role": "assistant",
            "content": chat_completion.choices[0].message.content,
        }
    )

    return chat_completion.choices[0].message.content.strip()


def extract_ports(compose_path):
    with open(compose_path, "r") as f:
        compose_data = yaml.safe_load(f)

    ports_info = []
    try:
        services = compose_data.get("services", {})
        for service_name, service_data in services.items():
            ports = service_data.get("ports", [])
            if ports:
                # Use first external port only (format like "8080:80" or "8080:80/tcp")
                first_port = ports[0].split(":")[0].split("/")[0]
                ports_info.append((service_name, first_port))
    except Exception as e:
        print(f"Warning: Could not extract ports from {compose_path}: {e}")
    return ports_info

def extract_traefik_domains(compose_data):
    """
    Extracts public domains from Traefik labels.

    Returns: dict of service_name -> [list of domains]
    """
    traefik_domains = {}

    services = compose_data.get("services", {})
    for service_name, service_data in services.items():
        labels = service_data.get("labels", [])

        if not labels:
            continue

        domains = []

        for label in labels:
            if isinstance(label, str):
                # Example:
                # traefik.http.routers.x.rule=Host(`example.com`)
                match = re.search(r"Host\(`([^`]+)`\)", label)
                if match:
                    domains.append(match.group(1))
            elif isinstance(label, dict):
                # Label dict format
                for k, v in label.items():
                    match = re.search(r"Host\(`([^`]+)`\)", v)
                    if match:
                        domains.append(match.group(1))

        if domains:
            traefik_domains[service_name] = domains

    return traefik_domains

def generate_markdown(service_folder_name, compose_content, ports_info, output_dir):
    # Build notes section with one line per service
    notes_lines = []
    # List of services to ignore when generating access notes
    ignored_access_notes_services = ["database"]
    # If the folder/file name contains '-disabled', skip all access notes
    if "-disabled" in service_folder_name:
        notes = "None"
    else:
        # --- Look for -api public URL in the compose file ---
        api_url_match = re.search(
            r"(https?://[\w\-]+-api\.jakefarrell\.ie)", compose_content
        )
        backend_url = None
        frontend_url = None
        image = None
        if api_url_match:
            backend_url = api_url_match.group(1)
            frontend_url = backend_url.replace("-api.jakefarrell.ie", ".jakefarrell.ie")
        # --- Look for any public URL or bare domain in env vars ---
        public_env_urls = {}  # service_name -> public_url or domain
        # Extract Traefik domains
        compose_data = yaml.safe_load(compose_content)
        traefik_domains = extract_traefik_domains(compose_data)

        notes_lines = []
        services = compose_data.get("services", {})

        for service_name in services.keys():
            
            if service_name in ignored_access_notes_services:
                continue

            # Traefik (highest priority)
            if service_name in traefik_domains:
                for domain in traefik_domains[service_name]:
                    url = f"https://{domain}"
                    notes_lines.append(
                        f"- Access `{service_name}` at [{url}]({url}) (Publicly Accessible via Traefik)"
                    )
                continue

            # Environment URL
            if service_name in public_env_urls:
                url = public_env_urls[service_name]
                notes_lines.append(
                    f"- Access `{service_name}` at [{url}]({url}) (Publicly Accessible)"
                )
                continue

            # Ports fallback
            matching_ports = [p for s, p in ports_info if s == service_name]
            if matching_ports:
                port = matching_ports[0]
                notes_lines.append(
                    f"- Access `{service_name}` at [http://cheeselab:{port}](http://cheeselab:{port}) (Local Network Only)"
                )
                continue

        # If nothing found
        notes = "\n".join(notes_lines) if notes_lines else "None"

            

    title_name = service_folder_name.replace("-", " ").title()
    title_name = title_name.replace("Ca298", "CA298")
    title_name = title_name.replace("Cablenetwork", "Cable Network")
    title_name = title_name.replace("Clubsandsocs", "Clubs & Socs")
    title_name = title_name.replace("Api", "API")
    title_name = title_name.replace("Dcu", "DCU")
    title_name = title_name.replace("Thecollegeview", "The College View")

    print(f"Generating description for: {title_name}")
    # check if description already exists to avoid unnecessary API calls
    existing_md_path = output_dir / f"{service_folder_name}.md"
    if existing_md_path.exists():
        existing_content = existing_md_path.read_text()
        desc_match = re.search(r"## Description\s+([\s\S]+?)\s+## Docker Compose File", existing_content)
        if desc_match:
            description = desc_match.group(1).strip()
            print(f"Using existing description for: {title_name}")
        else:
            description = get_chatbot_response(title_name + f" ({image})")
    else:
        description = get_chatbot_response(title_name + f" ({image})")
    # description = "This is a test"
    notes = notes.replace(
        "[http://cheeselab:1313](http://cheeselab:1313) (Local Network Only)",
        "[https://collegeguide-blog.jakefarrell.ie](https://collegeguide-blog.jakefarrell.ie) (Publicly Accessible)",
    )

    notes = notes.replace(
        "[http://cheeselab:802](http://cheeselab:802) (Local Network Only)",
        "[https://panel.cablenetwork.xyz](https://panel.cablenetwork.xyz) (Publicly Accessible)",
    )

    notes = notes.replace("http://cheeselab:9443", "https://cheeselab:9443")
    
    notes = notes.replace(
        "[http://cheeselab:6022](http://cheeselab:6022) (Local Network Only)",
        "[https://cablenetwork.jakefarrell.ie](https://cablenetwork.jakefarrell.ie) (Publicly Accessible)",
    )

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
    output_path.write_text(md_content)
    print(f"Generated: {output_path}")


if __name__ == "__main__":
    repo = "https://github.com/CheeseLad/vps.git"
    output_dir = "docs\\vps\\services"
    
    clone_and_run(repo, output_dir)
