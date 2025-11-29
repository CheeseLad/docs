# Nubar
    
    

## Description

Like a bouncing DVD logo from back in the day, but with pints of Guinness, what's not to like?

## Docker Compose File

```yaml
services:
  nubar:
    image: ghcr.io/cheeselad/nubar:latest
    container_name: nubar
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.nubar-site.entrypoints=https"
      - "traefik.http.routers.nubar-site.rule=Host(`www.nubar.xyz`)"
      - "traefik.http.routers.nubar-site-base-url.entrypoints=https"
      - "traefik.http.routers.nubar-site-base-url.rule=Host(`nubar.xyz`)"

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access `nubar` at [https://www.nubar.xyz](https://www.nubar.xyz) (Publicly Accessible via Traefik)
- Access `nubar` at [https://nubar.xyz](https://nubar.xyz) (Publicly Accessible via Traefik)