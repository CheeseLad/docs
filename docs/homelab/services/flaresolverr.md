# Flaresolverr
    
    

## Description

Flaresolverr is a lightweight, open-source proxy server that helps bypass Cloudflare's restrictions on accessing certain websites. Its main purpose is to make it easier to access content that's blocked by Cloudflare, often used in homelabs and home servers. Flaresolverr can solve Cloudflare's challenges, such as CAPTCHAs, and can be integrated with other services like torrent clients and download managers. By using Flaresolverr, users can access and download content from websites that would otherwise be inaccessible due to Cloudflare's protection mechanisms.

## Docker Compose File

```yaml
services:
  flaresolverr:
    image: ghcr.io/flaresolverr/flaresolverr:latest
    container_name: flaresolverr
    environment:
      - LOG_LEVEL=info
      - LOG_HTML=false
      - CAPTCHA_SOLVER=none
      - TZ=Europe/Dublin
    ports:
      - 8191:8191
    networks:
      - cheeselab
    restart: unless-stopped

networks:
  cheeselab:
    external: true

```

## Notes

- Access `flaresolverr` at [http://cheeselab:8191](http://cheeselab:8191) (Local Network Only)