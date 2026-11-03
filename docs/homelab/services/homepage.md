# Homepage
    
    

## Description

Homepage is a simple web-based interface for managing and accessing your homelab services. Its main purpose is to provide a centralized hub for all your self-hosted applications, making it easy to navigate and launch them. With Homepage, you can customize the layout, add bookmarks, and even set up authentication for added security. This service is super useful for keeping all your homelab services organized and easily accessible from one place.

## Docker Compose File

```yaml
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    restart: unless-stopped
    user: "1000:996"
    environment:
      - HOMEPAGE_ALLOWED_HOSTS=home.jakefarrell.ie,local.jakefarrell.ie
      - HOMEPAGE_VAR_IMMICH=$HOMEPAGE_VAR_IMMICH
      - HOMEPAGE_VAR_JACKETT=$HOMEPAGE_VAR_JACKETT
      - HOMEPAGE_VAR_PAPERLESS_NGX=$HOMEPAGE_VAR_PAPERLESS_NGX
      - HOMEPAGE_VAR_PI_HOLE=$HOMEPAGE_VAR_PI_HOLE
      - HOMEPAGE_VAR_JELLYFIN=$HOMEPAGE_VAR_JELLYFIN
      - HOMEPAGE_VAR_SONARR=$HOMEPAGE_VAR_SONARR
      - HOMEPAGE_VAR_RADARR=$HOMEPAGE_VAR_RADARR
      - HOMEPAGE_VAR_LIDARR=$HOMEPAGE_VAR_LIDARR
      - HOMEPAGE_VAR_TRANSMISSION=$HOMEPAGE_VAR_TRANSMISSION
      - HOMEPAGE_VAR_PORTAINER=$HOMEPAGE_VAR_PORTAINER
      - HOMEPAGE_VAR_SPEEDTEST_TRACKER=$HOMEPAGE_VAR_SPEEDTEST_TRACKER
    volumes:
      - ~/storage/homepage/config:/app/config
      - ~/storage/homepage/images:/app/public/images
      - /var/run/docker.sock:/var/run/docker.sock:ro
    ports:
      - "3231:3000"
```

## Notes

- Access `homepage` at [https://home.jakefarrell.ie](https://home.jakefarrell.ie) (Publicly Accessible)