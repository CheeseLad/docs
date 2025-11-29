# CA298 Pizzashop
    
    

## Description

CA298 Project 1: Django Frontend & Backend: Grade 100% 

## Docker Compose File

```yaml
services:
  ca298-pizzashop:
    image: ghcr.io/cheeselad/ca298-pizzashop:latest
    container_name: ca298-pizzashop
    hostname: ca298-pizzashop
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.ca298-pizzashop.entrypoints=https"
      - "traefik.http.routers.ca298-pizzashop.rule=Host(`pizzashop.jakefarrell.ie`)"

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access `ca298-pizzashop` at [https://pizzashop.jakefarrell.ie](https://pizzashop.jakefarrell.ie) (Publicly Accessible via Traefik)