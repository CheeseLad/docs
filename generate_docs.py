import yaml
from pathlib import Path
from groq import Groq
import re
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

system_prompt = {
    "role": "system",
    "content": "Your job is to write a maximum of 4 sentences about the home server / homelab service name provided by the user. Give a brief description of the service, its purpose, and any useful features. Not too formal.",
}


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


def generate_markdown(service_folder_name, compose_content, ports_info, output_dir):
    # Build notes section with one line per service
    notes_lines = []
    # List of services to ignore when generating access notes
    ignored_access_notes_services = ["collegeguide-redis", "wings", "mysql-database"]
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
        try:
            compose_data = yaml.safe_load(compose_content)
            image = compose_data.get("services", {}).get(service_folder_name, {}).get("image", service_folder_name)
            services = compose_data.get("services", {})
            for service_name, service_data in services.items():
                envs = service_data.get("environment", [])
                for env in envs:
                    if isinstance(env, str):
                        # Prefer full URL if present
                        url_match = re.search(r"https?://[\w\-\.]+\.[a-z]{2,}", env)
                        if url_match and service_name not in public_env_urls:
                            public_env_urls[service_name] = url_match.group(0)
                        # Otherwise, look for bare domain
                        if service_name not in public_env_urls:
                            for part in re.split(r"[=, ]", env):
                                if re.match(
                                    r"[\w\-\.]+\.[a-z]{2,}$", part
                                ) and not part.startswith("http"):
                                    public_env_urls[service_name] = f"https://{part}"
                                    break
                    elif isinstance(env, dict):
                        for k, v in env.items():
                            if isinstance(v, str):
                                url_match = re.search(
                                    r"https?://[\w\-\.]+\.[a-z]{2,}", v
                                )
                                if url_match and service_name not in public_env_urls:
                                    public_env_urls[service_name] = url_match.group(0)
                                if service_name not in public_env_urls:
                                    for part in re.split(r"[=, ]", v):
                                        if re.match(
                                            r"[\w\-\.]+\.[a-z]{2,}$", part
                                        ) and not part.startswith("http"):
                                            public_env_urls[service_name] = (
                                                f"https://{part}"
                                            )
                                            break
                # If we didn't find URLs in parsed env vars, search the raw compose content for this service
                if service_name not in public_env_urls:
                    # Try a simpler approach - just search for the service name and environment section
                    service_start = compose_content.find(f"{service_name}:")
                    if service_start != -1:
                        # Find the environment section after this service
                        env_start = compose_content.find("environment:", service_start)
                        if env_start != -1:
                            # Find the next section or end of file
                            next_section = compose_content.find("\n  ", env_start + 20)
                            if next_section == -1:
                                next_section = len(compose_content)
                            env_section = compose_content[env_start:next_section]
                            # Look for URLs in the raw environment section
                            url_matches = re.findall(
                                r"https?://[\w\-\.]+\.[a-z]{2,}", env_section
                            )
                            if url_matches:
                                public_env_urls[service_name] = url_matches[0]
        except Exception as e:
            print(
                f"Warning: Could not extract public env URLs from compose_content: {e}"
            )
        # --- End new logic ---
        for service_name, port in ports_info:
            # Skip services in the ignored list
            if service_name in ignored_access_notes_services:
                continue
            # If we found an -api URL, use the public URLs for frontend/backend
            if backend_url and frontend_url:
                if "frontend" in service_name:
                    notes_lines.append(
                        f"- Access `{service_name}` at [{frontend_url}]({frontend_url}) (Publicly Accessible)"
                    )
                elif "backend" in service_name:
                    notes_lines.append(
                        f"- Access `{service_name}` at [{backend_url}]({backend_url}) (Publicly Accessible)"
                    )
                else:
                    notes_lines.append(
                        f"- Access `{service_name}` at [http://cheeselab:{port}](http://cheeselab:{port}) (Local Network Only)"
                    )
            elif service_name in public_env_urls:
                notes_lines.append(
                    f"- Access `{service_name}` at [{public_env_urls[service_name]}]({public_env_urls[service_name]}) (Publicly Accessible)"
                )
            else:
                notes_lines.append(
                    f"- Access `{service_name}` at [http://cheeselab:{port}](http://cheeselab:{port}) (Local Network Only)"
                )
        notes = "\n".join(notes_lines) if notes_lines else "None"

    title_name = service_folder_name.replace("-", " ").title()
    title_name = title_name.replace("Ca298", "CA298")
    title_name = title_name.replace("Cablenetwork", "Cable Network")
    title_name = title_name.replace("Collegeguide", "CollegeGuide")
    title_name = title_name.replace("Mysql", "MySQL")
    title_name = title_name.replace("Ddclient", "DDClient")
    title_name = title_name.replace("Reactexam", "React Exam")
    title_name = title_name.replace("Universitysystem", "University System")

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


if __name__ == "__main__":
    services_dir = "Y:\\home\\jake\\services"
    output_dir = "docs\\homelab\\services"

    main(services_dir, output_dir)
