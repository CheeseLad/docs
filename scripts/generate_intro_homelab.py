from pathlib import Path
import re

def main(services_dir, output_file, excluded_services):
    services_dir = Path(services_dir)
    output_file = Path(output_file)
    
    service_list = []

    for markdown_file in services_dir.glob("*.md"):
        with open(markdown_file, "r") as f:
            content = f.read()
            heading_match = re.search(r"# (.+)", content)
            if heading_match:
                service_name = heading_match.group(1).strip()
                if service_name.lower().replace(" ", "-") not in excluded_services:
                  service_list.append(f"- [{service_name}](./services/{markdown_file.name})\n")
                
    sorted_service_list = sorted(service_list)
    md_content = f"""# Jake Farrell's Homelab Setup

## Introduction

My Homelab consists of a Dell OptiPlex 5060 SFF running Debian 13 Trixie that was saved from an e-waste bin in my college. I have been using it to host various services and applications that I use on a daily basis. Configs for many of these services can be found in the `services` directory.

## Specs

- **Model**: Dell OptiPlex 5060 SFF
- **OS**: Debian 13 Trixie
- **CPU**: Intel Core i5-8400
- **RAM**: 48GB DDR4 2400MHz (2x 16GB, 2x 8GB)
- **Storage**: 256GB NVMe SSD, 2TB HDD, 6TB HDD
- **Offsite Backup**: Rclone encrypted to Google Drive

## Services (Docker)

{''.join(sorted_service_list)}
## Services (Native)

- [PiVPN](https://www.pivpn.io/)
- [Samba](https://www.samba.org/)
- [Rclone](https://rclone.org/)
"""

    output_file.write_text(md_content)
    print(f"Generated: {output_file}")
  


if __name__ == "__main__":
    services_dir = "../docs/homelab/services"
    output_file = "../docs/homelab/info.md"

    excluded_services = [
      "jackett", 
      "transmission",
      "wiki-dcu-lol",
      "better-file-search-website",
      "bfs-postgres",
    ]

    main(services_dir, output_file, excluded_services)