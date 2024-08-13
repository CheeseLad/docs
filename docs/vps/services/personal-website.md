# Personal Website

## Description

*My personal portfolio website*


### Tech Stack Used:
- Svelte
- TailwindCSS
- Docker

### Website Content & Features:
- Contact Information
- Recent Projects
- Related Experience
- Tech Stack

## Docker Compose File

```yaml
services:
  portfolio-svelte:
    image: ghcr.io/cheeselad/portfolio-svelte:latest
    container_name: portfolio-svelte
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.portfolio-svelte.entrypoints=https"
      - "traefik.http.routers.portfolio-svelte.rule=Host(`portfolio.jakefarrell.ie`)"
      - "traefik.http.routers.personal-site.entrypoints=https"
      - "traefik.http.routers.personal-site.rule=Host(`www.jakefarrell.ie`)"
      - "traefik.http.routers.personal-site-base-url.entrypoints=https"
      - "traefik.http.routers.personal-site-base-url.rule=Host(`jakefarrell.ie`)"

  watchtower-portfolio-svelte:
    image: containrrr/watchtower
    container_name: watchtower-portfolio-svelte
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --interval 600

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access my Personal Website here: [`https://jakefarrell.ie`](https://jakefarrell.ie)