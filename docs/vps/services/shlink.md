# Shlink
    
    

## Description

Shlink is a virtual private server (VPS) service that allows you to run your own URL shortener. Its purpose is to provide a self-hosted alternative to public URL shortening services, giving you control over your links and data. With Shlink, you can create custom short URLs, track clicks, and manage your links from a simple web interface. It's a great option for those who want a private and customizable URL shortening solution.

## Docker Compose File

```yaml
services:
  shlink:
    image: shlinkio/shlink:stable
    restart: unless-stopped
    container_name: shlink
    environment:
      - TZ="Europe/Dublin"
      - DEFAULT_DOMAIN=s.jakefarrell.ie
      - IS_HTTPS_ENABLED=true
      - GEOLITE_LICENSE_KEY=${GEOLITE_LICENSE_KEY}
      - DB_DRIVER=mysql
      - DB_USER=${DB_USER}
      - DB_NAME=${DB_NAME}
      - DB_PASSWORD=${DB_PASSWORD}
      - DB_HOST=${DB_HOST}
      - SHELL_VERBOSITY=3
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.shlink.entrypoints=https"
      - "traefik.http.routers.shlink.rule=Host(`s.jakefarrell.ie`)"

  shlink-web-client:
    image: shlinkio/shlink-web-client
    restart: unless-stopped
    container_name: shlink-web-client
    volumes:
      - ./servers.json:/usr/share/nginx/html/servers.json
    depends_on:
      - shlink
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.shlink-gui.entrypoints=https"
      - "traefik.http.routers.shlink-gui.rule=Host(`shlink.jakefarrell.ie`)"

networks:
  default:
    name: traefik_net
    external: true

```

## Notes

- Access `shlink` at [https://s.jakefarrell.ie](https://s.jakefarrell.ie) (Publicly Accessible via Traefik)
- Access `shlink-web-client` at [https://shlink.jakefarrell.ie](https://shlink.jakefarrell.ie) (Publicly Accessible via Traefik)