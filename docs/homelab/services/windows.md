# Windows
    
    

## Description

Windows is a Docker image provided by dockurr, allowing users to run a Windows environment within a container. This service enables users to test, develop, and deploy Windows-specific applications in a controlled and isolated space. The Windows Docker image supports various versions of Windows, including Server Core and Desktop, making it a versatile tool for developers and testers. By using this image, users can leverage the benefits of containerization, such as easy deployment and management, for their Windows-based applications.

## Docker Compose File

```yaml
services:
  windows:
    image: dockurr/windows
    container_name: windows
    environment:
      VERSION: "11"
      DISK_SIZE: "64G"
      RAM_SIZE: "4G"
      CPU_CORES: "3"
      USERNAME: $USERNAME
      PASSWORD: $PASSWORD
      LANGUAGE: "English"
      REGION: "en-GB"
      KEYBOARD: "en-GB"
    devices:
      - /dev/kvm
      - /dev/net/tun
    cap_add:
      - NET_ADMIN
    ports:
      - 8006:8006
      - 3389:3389/tcp
      - 3389:3389/udp
    volumes:
      - ~/storage/windows:/storage
    restart: unless-stopped
    stop_grace_period: 2m
```

## Notes

- Access `windows` at [http://cheeselab:8006](http://cheeselab:8006) (Local Network Only)