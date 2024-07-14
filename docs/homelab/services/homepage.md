# Homepage

## Description

A modern, fully static, fast, secure fully proxied, highly customizable application dashboard with integrations for over 100 services and translations into multiple languages. Easily configured via YAML files or through docker label discovery. 

## Docker Compose File

```yaml
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    hostname: homepage
    restart: unless-stopped
    volumes:
      - /home/jake/services/homepage/config:/app/config
      - /var/run/docker.sock:/var/run/docker.sock
      - /home/jake/services/homepage/images:/app/public/images
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.homepage.entrypoints=https"
      - "traefik.http.routers.homepage.rule=Host(`local.jakefarrell.ie`)"
networks:
  default:
    external:
      name: traefik_net
```

## Notes

- Access Homepage at [https://local.jakefarrell.ie](https://local.jakefarrell.ie) (Local Network Only)