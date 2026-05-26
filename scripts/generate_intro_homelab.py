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

My homelab consists of a Dell Optiplex 5060 running Debian 12 that was saved from an e-waste bin in my college. I have been using it to host various services and applications that I use on a daily basis. Configs for many of these services can be found in the `services` directory.

## Specs

- **Model**: Dell Optiplex 5060
- **OS**: Debian 12
- **CPU**: Intel Core i3-8100
- **RAM**: 16GB DDR4
- **Storage**: 256GB NVMe SSD, 6TB HDD
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
    services_dir = "docs\\homelab\\services"
    output_file = "docs\\homelab\\info.md"
    
    excluded_services = [
      "immich", 
      "jackett", 
      "lidarr",
      "photoprism",
      "radarr",
      "sonarr",
      "transmission",
      "wiki-dcu-lol"
    ]

    main(services_dir, output_file, excluded_services)