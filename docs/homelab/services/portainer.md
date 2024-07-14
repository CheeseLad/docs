# Portainer

## Description

Portainer Community Edition is a lightweight service delivery platform for containerized applications that can be used to manage Docker, Swarm, Kubernetes and ACI environments. It is designed to be as simple to deploy as it is to use. The application allows you to manage all your orchestrator resources (containers, images, volumes, networks and more) through a ‘smart’ GUI and/or an extensive API.


## Docker Compose File

```yaml
services:
  portainer:
    container_name: portainer
    hostname: portainer
    image: portainer/portainer-ce:latest
    ports:
      - 9443:9443
    volumes:
      - ./config/data:/data
      - /var/run/docker.sock:/var/run/docker.sock
    restart: unless-stopped
    
volumes:
  data:
```

## Notes

- Access Portainer at `https://cheeselab:9443` (Local Network Only)
- Web UI only works with HTTPS, so you need to use `https://` instead of `http://`, certificate is not required.