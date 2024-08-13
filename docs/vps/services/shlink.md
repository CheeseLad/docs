# Shlink

## Description

Shlink is a self-hosted URL shortener that allows you to shorten URLs and serve them under your own domain. The application is built using PHP and MySQL and is designed to be lightweight and easy to use.

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

- Access Shlink here: [`https://shlink.jakefarrell.ie`](https://shlink.jakefarrell.ie)