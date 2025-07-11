# Dozzle
    
    

## Description

Dozzle is a homelab service that provides a web-based interface for viewing and managing container logs. Its main purpose is to make it easy to monitor and debug containers, allowing you to view logs from multiple containers in one place. Dozzle supports popular container runtimes like Docker, Podman, and Kubernetes, and offers features like log filtering and live updates. This makes it a useful tool for homelab enthusiasts and developers who need to keep an eye on their containerized applications.

## Docker Compose File

```yaml
services:
  dozzle:
    container_name: dozzle
    image: amir20/dozzle:latest
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - 8087:8080
    networks:
      - cheeselab
    restart: unless-stopped

networks:
  cheeselab:
    external: true
```

## Notes

- Access `dozzle` at [http://cheeselab:8087](http://cheeselab:8087) (Local Network Only)