# Sonarr

## Description

Sonarr is a PVR for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort, and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

## Docker Compose File

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    hostname: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - /home/jake/services/sonarr/config:/config
      - /mnt/usb1/Plex/Series:/tv
      - /home/jake/downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```

## Notes

- Access Sonarr at `http://cheeselab:8989` (Local Network Only)