# DCU Fotosoc Website

## Docker Compose File

```yaml
services:
  dcufotosoc-website:
    image: ghcr.io/cheeselad/fotosoc:latest
    container_name: dcufotosoc-website
    hostname: dcufotosoc-website
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.dcufotosoc-website.entrypoints=https"
      - "traefik.http.routers.dcufotosoc-website.rule=Host(`dcufotosoc.jakefarrell.ie`)"

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access thee DCU Fotosoc website here: [`https://dcufotosoc.jakefarrell.ie`](https://dcufotosoc.jakefarrell.ie)