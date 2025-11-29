# Portfolio
    
    

## Description

*My personal portfolio website*


## Tech Stack Used:
- Vite
- TailwindCSS
- Docker

## Website Content & Features:
- Contact Information
- Recent Projects
- Related Experience
- Tech Stack

## Docker Compose File

```yaml
services:
  portfolio:
    image: ghcr.io/cheeselad/portfolio:latest
    container_name: portfolio
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.portfolio-svelte.entrypoints=https"
      - "traefik.http.routers.portfolio-svelte.rule=Host(`portfolio.jakefarrell.ie`)"
      - "traefik.http.routers.personal-site.entrypoints=https"
      - "traefik.http.routers.personal-site.rule=Host(`www.jakefarrell.ie`)"
      - "traefik.http.routers.personal-site-base-url.entrypoints=https"
      - "traefik.http.routers.personal-site-base-url.rule=Host(`jakefarrell.ie`)"

networks:
  default:
    name: traefik_net
    external: true

```

## Notes

- Access `portfolio` at [https://portfolio.jakefarrell.ie](https://portfolio.jakefarrell.ie) (Publicly Accessible via Traefik)
- Access `portfolio` at [https://www.jakefarrell.ie](https://www.jakefarrell.ie) (Publicly Accessible via Traefik)
- Access `portfolio` at [https://jakefarrell.ie](https://jakefarrell.ie) (Publicly Accessible via Traefik)