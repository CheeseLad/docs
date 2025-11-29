# Macos
    
    

## Description

Dockurr/macos is a Docker image that allows you to run macOS in a container, giving you a virtualized macOS environment for testing, development, and other purposes. This service enables you to use macOS on non-Apple devices or run multiple macOS instances on a single machine. The image includes a fully functional macOS setup, complete with a graphical user interface and support for various macOS applications. By using Dockurr/macos, you can create a homelab setup for experimenting with macOS without the need for dedicated Apple hardware.

## Docker Compose File

```yaml
services:
  macos:
    image: dockurr/macos
    container_name: macos
    environment:
      VERSION: "14"
      DISK_SIZE: "64G"
      RAM_SIZE: "4G"
      CPU_CORES: "3"
    devices:
      - /dev/kvm
      - /dev/net/tun
    cap_add:
      - NET_ADMIN
    ports:
      - 8007:8006
      - 5900:5900/tcp
      - 5900:5900/udp
    volumes:
      - ~/storage/macos:/storage
    restart: unless-stopped
    stop_grace_period: 2m
```

## Notes

- Access `macos` at [http://cheeselab:8007](http://cheeselab:8007) (Local Network Only)