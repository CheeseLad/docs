# DCU Media Production Society Website

## Docker Compose File

```yaml
services:
  dcumps-website:
    image: ghcr.io/dcumps/dcumps-website-django:latest
    container_name: dcumps-website
    hostname: dcumps-website
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.dcumps-website.entrypoints=https"
      - "traefik.http.routers.dcumps-website.rule=Host(`www.dcumps.ie`)"
      - "traefik.http.routers.dcumps-website.tls.certresolver=dcumps"
      - "traefik.http.routers.dcumps-website-base-url.entrypoints=https"
      - "traefik.http.routers.dcumps-website-base-url.rule=Host(`dcumps.ie`)"
      - "traefik.http.routers.dcumps-website-base-url.tls.certresolver=dcumps"

networks:
  default:
    external:
      name: traefik_net
```

## Notes

- Access the DCU Media Production Society website here: [`https://dcumps.ie`](https://dcumps.ie)