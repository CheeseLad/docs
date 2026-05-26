# Radarr
    
    

## Description

Radarr is a popular homelab service that helps you manage your movie collection by automatically searching for and downloading new releases. Its purpose is to simplify the process of keeping your library up-to-date, so you can easily access and enjoy your favorite movies. With features like automated movie searching, download management, and integration with other services like Plex, Radarr makes it easy to maintain a organized and curated movie library. By using Radarr, you can save time and effort, and focus on enjoying your movies rather than searching for them.

## Docker Compose File

```yaml
services:
  radarr:
    image: lscr.io/linuxserver/radarr:latest
    container_name: radarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - ~/storage/radarr:/config
      - /mnt/storage-hdd/Media/Movies:/movies
      - /mnt/storage-hdd/Downloads:/downloads
    ports:
      - 7878:7878
    networks:
      - cheeselab
    restart: unless-stopped

networks:
  cheeselab:
    external: true
```

## Notes

- Access `radarr` at [http://cheeselab:7878](http://cheeselab:7878) (Local Network Only)