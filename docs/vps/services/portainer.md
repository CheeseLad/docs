# Portainer
    
    

## Description

Portainer is a popular, open-source container management platform that makes it easy to manage Docker, Swarm, and Kubernetes environments. Its main purpose is to provide a simple, user-friendly interface for deploying, managing, and monitoring containers. With Portainer, you can easily create and manage containers, volumes, and networks, as well as monitor resource usage and performance. It's a great tool for anyone looking to simplify their container management workflow and make the most of their VPS or server resources.

## Docker Compose File

```yaml
services:
  portainer:
    container_name: portainer
    hostname: portainer
    image: portainer/portainer-ce:latest
    volumes:
      - ./data:/data
      - /var/run/docker.sock:/var/run/docker.sock
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.portainer.rule=Host(`portainer.jakefarrell.ie`)"
      - "traefik.http.routers.portainer.entrypoints=https"
      - "traefik.http.services.portainer.loadbalancer.server.port=9000"
      - "traefik.http.routers.portainer.service=portainer"
    
volumes:
  data:

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access `portainer` at [https://portainer.jakefarrell.ie](https://portainer.jakefarrell.ie) (Publicly Accessible via Traefik)