# Jackett
    
    

## Description

Jackett is a popular service for homelabs that acts as a proxy server to index torrent sites, making it easy to search and find torrents from various sources. Its purpose is to simplify the process of finding and downloading torrents by providing a unified search interface. Jackett supports a wide range of torrent sites and can be integrated with other homelab services like Sonarr and Radarr for automated media management. By using Jackett, users can easily find and download their favorite movies, TV shows, and other content without having to visit multiple torrent sites.

## Docker Compose File

```yaml
services:
  jackett:
    container_name: jackett
    image: linuxserver/jackett
    restart: unless-stopped
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - AUTO_UPDATE=true
    ports:
      - 9117:9117
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - ~/storage/jackett:/config/Jackett
      - /mnt/storage-hdd/Downloads:/downloads
    networks:
      - cheeselab

networks:
  cheeselab:
    external: true
```

## Notes

- Access `jackett` at [http://cheeselab:9117](http://cheeselab:9117) (Local Network Only)