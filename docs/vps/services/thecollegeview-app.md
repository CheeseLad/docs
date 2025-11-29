# The College View App
    
    

## Description

Developing an iOS & Android app for The College View - DCU's independent student newspaper using Flutter and the WordPress REST API. The app allows users to view articles and categories, submit their own articles and search for articles, the app is planned to be released on both the Apple App Store and the Google Play Store.

## Docker Compose File

```yaml
services:
  thecollegeview-app:
    image: nginx:latest
    container_name: thecollegeview-app
    hostname: thecollegeview-app
    restart: unless-stopped
    volumes:
      - ./html:/usr/share/nginx/html
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.thecollegeview-app.entrypoints=https"
      - "traefik.http.routers.thecollegeview-app.rule=Host(`tcvapp.jakefarrell.ie`)"

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access `thecollegeview-app` at [https://tcvapp.jakefarrell.ie](https://tcvapp.jakefarrell.ie) (Publicly Accessible via Traefik)