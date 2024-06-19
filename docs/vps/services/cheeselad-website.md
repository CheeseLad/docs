# CheeseLad Website

## Docker Compose File

```yaml
services:
  cheeselad-website:
    image: nginx:latest
    container_name: cheeselad-website
    hostname: cheeselad-website
    restart: unless-stopped
    volumes:
      - ./html:/usr/share/nginx/html
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.cheeselad-website.entrypoints=https"
      - "traefik.http.routers.cheeselad-website.rule=Host(`www.cheeselad.xyz`)"
      - "traefik.http.routers.cheeselad-website-base-url.entrypoints=https"
      - "traefik.http.routers.cheeselad-website-base-url.rule=Host(`cheeselad.xyz`)"

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access CheeseLad's website here: [`https://cheeselad.xyz`](https://cheeselad.xyz)