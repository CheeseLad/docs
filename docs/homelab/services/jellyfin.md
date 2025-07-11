# Jellyfin
    
    

## Description

Jellyfin is a free, open-source media server that allows you to organize and stream your favorite movies, TV shows, and music to various devices. Its purpose is to provide a self-hosted alternative to popular streaming services like Plex, giving you full control over your media library. With Jellyfin, you can access your media from anywhere, using a web-based interface or mobile apps, and it also supports features like live TV, DVR, and subtitles. It's a great option for those who want to manage their own media collection without relying on third-party services.

## Docker Compose File

```yaml
---
services:
  jellyfin:
    image: lscr.io/linuxserver/jellyfin:latest
    container_name: jellyfin
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - JELLYFIN_PublishedServerUrl=http://192.168.1.2
    volumes:
      - ~/storage/jellyfin:/config
      - /mnt/storage-hdd/Media:/media
    ports:
      - 8096:8096
      - 8920:8920
      - 7359:7359/udp
     # - 1900:1900/udp
    networks:
      - cheeselab
    restart: unless-stopped

networks:
  cheeselab:
    external: true
```

## Notes

- Access `jellyfin` at [http://cheeselab:8096](http://cheeselab:8096) (Local Network Only)