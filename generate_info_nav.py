import re
from pathlib import Path
import yaml

INFO_FILE = "docs/homelab/info.md"
MKDOCS_FILE = "mkdocs.yml"

def extract_services_from_info(info_path):
    """Extract markdown links from the Services (Docker) section."""
    content = Path(info_path).read_text(encoding="utf-8")

    docker_section = re.search(
        r"## Services \(Docker\)(.*?)(##|$)", content, re.DOTALL
    )
    if not docker_section:
        raise ValueError("Could not find Services (Docker) section in info.md")

    section_text = docker_section.group(1)

    # Extract markdown links
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", section_text)

    return [
        {name: f"homelab/{path.strip('./')}"}
        for name, path in links
    ]


def update_mkdocs_nav(mkdocs_path, services):
    with open(mkdocs_path, "r", encoding="utf-8") as f:
        mkdocs = yaml.safe_load(f)

    nav = mkdocs.get("nav", [])

    # Find the nav → Homelab → Service Information section
    for item in nav:
        if isinstance(item, dict) and "Homelab" in item:
            homelab_section = item["Homelab"]
            for sub in homelab_section:
                if isinstance(sub, dict) and "Service Information" in sub:
                    sub["Service Information"] = services
                    break

    # Dump YAML
    yaml_output = yaml.dump(mkdocs, sort_keys=False, allow_unicode=True)

    # Fix indentation: all service items should have EXACTLY 6 spaces before "- "
    yaml_output = re.sub(
        r"^(\s{4}- )",     # YAML default for this list is 4 spaces
        r"      - ",       # Replace with exactly 6 spaces
        yaml_output,
        flags=re.MULTILINE
    )

    with open(mkdocs_path, "w", encoding="utf-8") as f:
        f.write(yaml_output)

    print("mkdocs.yml updated with correct indentation!")


if __name__ == "__main__":
    services = extract_services_from_info(INFO_FILE)
    update_mkdocs_nav(MKDOCS_FILE, services)
