# Radarr

## Description

Radarr is a movie management tool that automatically grabs movies from various sources and organizes them in a way that is easy to manage. It is a fork of Sonarr and works in a similar way. Radarr can be used to automatically download movies from various sources such as Usenet and BitTorrent.

## Docker Compose File

```yaml
services:
  radarr:
    image: lscr.io/linuxserver/radarr:latest
    container_name: radarr
    hostname: radarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - /home/jake/services/radarr/config:/config
      - /mnt/usb2/Plex/Movies:/movies
      - /home/jake/downloads:/downloads
    ports:
      - 7878:7878
    restart: unless-stopped
```

## Notes

- Access Radarr at `http://cheeselab:7878` (Local Network Only)