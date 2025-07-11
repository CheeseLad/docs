#!/usr/bin/env python3
"""
Script to populate the Docker services section in homelab/info.md
and the navigation in mkdocs.yml with all markdown files from homelab/services directory.
"""

import os
import re
from pathlib import Path

# List of service markdown filenames to ignore
IGNORED_SERVICES = [
    'immich.md',
    'jackett.md',
    'lidarr.md',
    'nginx.md',
    'photoprism.md',
    'radarr.md',
    'sonarr.md',
    'the-experiment.md',
    'transmission.md',
]

def extract_service_name(md_file_path):
    """Extract service name from the first line of a markdown file."""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            # Remove the # and any leading/trailing whitespace
            service_name = first_line.lstrip('#').strip()
            return service_name
    except Exception as e:
        print(f"Error reading {md_file_path}: {e}")
        # Fallback to filename without extension
        return Path(md_file_path).stem

def get_services_from_directory(services_dir):
    """Get all markdown files from the services directory and extract their names."""
    services = []
    
    if not os.path.exists(services_dir):
        print(f"Services directory not found: {services_dir}")
        return services
    
    for file in os.listdir(services_dir):
        if file.endswith('.md') and file not in IGNORED_SERVICES:
            file_path = os.path.join(services_dir, file)
            service_name = extract_service_name(file_path)
            services.append({
                'name': service_name,
                'filename': file,
                'path': f"./services/{file}",
                'mkdocs_path': f"homelab/services/{file}"
            })
    
    # Sort services alphabetically by name
    services.sort(key=lambda x: x['name'].lower())
    return services

def update_info_md(info_md_path, services):
    """Update the info.md file with the new services list."""
    
    # Read the current content
    with open(info_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the Docker services section
    # Look for the pattern that starts with "## Services (Docker)" and ends before "## Services (Native)"
    docker_section_pattern = r'(## Services \(Docker\)\n\n)(.*?)(\n\n## Services \(Native\))'
    match = re.search(docker_section_pattern, content, re.DOTALL)
    
    if not match:
        print("Could not find Docker services section in info.md")
        return False
    
    # Generate the new services list
    services_list = []
    for service in services:
        services_list.append(f"- [{service['name']}]({service['path']})")
    
    # Create the new content
    new_services_content = '\n'.join(services_list)
    new_content = match.group(1) + new_services_content + match.group(3)
    
    # Replace the old content with the new content
    updated_content = re.sub(docker_section_pattern, new_content, content, flags=re.DOTALL)
    
    # Write the updated content back to the file
    with open(info_md_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    return True

def update_mkdocs_yml(mkdocs_path, services):
    """Update the mkdocs.yml file with the new services navigation."""
    
    # Read the current content
    with open(mkdocs_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the Service Information section under Homelab
    # Look for the pattern that starts with "Service Information:" and ends before the next top-level item
    service_info_pattern = r'(    - Service Information:\n)(.*?)(\n    - Devices:)'
    match = re.search(service_info_pattern, content, re.DOTALL)
    
    if not match:
        print("Could not find Service Information section in mkdocs.yml")
        return False
    
    # Generate the new services list for mkdocs
    services_list = []
    for service in services:
        services_list.append(f"      - {service['name']}: {service['mkdocs_path']}")
    
    # Create the new content
    new_services_content = '\n'.join(services_list)
    new_content = match.group(1) + new_services_content + match.group(3)
    
    # Replace the old content with the new content
    updated_content = re.sub(service_info_pattern, new_content, content, flags=re.DOTALL)
    
    # Write the updated content back to the file
    with open(mkdocs_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    return True

def main():
    # Define paths
    script_dir = Path(__file__).parent
    services_dir = script_dir / "docs" / "homelab" / "services"
    info_md_path = script_dir / "docs" / "homelab" / "info.md"
    mkdocs_path = script_dir / "mkdocs.yml"
    
    print(f"Scanning services directory: {services_dir}")
    
    # Get all services
    services = get_services_from_directory(services_dir)
    
    if not services:
        print("No markdown files found in services directory")
        return
    
    print(f"Found {len(services)} services:")
    for service in services:
        print(f"  - {service['name']} ({service['filename']})")
    
    # Update the info.md file
    print(f"\nUpdating {info_md_path}...")
    if update_info_md(info_md_path, services):
        print("Successfully updated info.md with all services!")
    else:
        print("Failed to update info.md")
    
    # Update the mkdocs.yml file
    print(f"\nUpdating {mkdocs_path}...")
    if update_mkdocs_yml(mkdocs_path, services):
        print("Successfully updated mkdocs.yml with all services!")
    else:
        print("Failed to update mkdocs.yml")

if __name__ == "__main__":
    main() 