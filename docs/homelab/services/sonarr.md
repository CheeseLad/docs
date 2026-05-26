# Sonarr
    
    

## Description

Sonarr is a handy service that helps you manage your TV shows, automatically searching for and downloading new episodes as they become available. Its main purpose is to make it easy to keep your TV show library up to date, so you can focus on watching instead of searching. With features like episode tracking, automatic downloads, and integration with other homelab services, Sonarr is a great addition to any home server setup. By using Sonarr, you can streamline your TV show management and enjoy a more seamless viewing experience.

## Docker Compose File

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - ~/storage/sonarr:/config
      - /mnt/storage-hdd/Media/Series:/tv
      - /mnt/storage-hdd/Downloads:/downloads
    ports:
      - 8989:8989
    networks:
      - cheeselab
    restart: unless-stopped

networks:
  cheeselab:
    external: true

```

## Notes

- Access `sonarr` at [http://cheeselab:8989](http://cheeselab:8989) (Local Network Only)