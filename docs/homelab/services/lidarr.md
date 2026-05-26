# Lidarr
    
    

## Description

Lidarr is a popular music collection manager that helps you organize and maintain your music library. Its purpose is to automatically fetch metadata, such as artist and album information, and download album artwork for your music files. Lidarr also allows you to manage multiple music libraries and supports various music formats, making it a useful tool for music enthusiasts. With features like automated metadata tagging and artwork download, Lidarr simplifies the process of keeping your music collection up-to-date and organized.

## Docker Compose File

```yaml
services:
  lidarr:
    image: lscr.io/linuxserver/lidarr:latest
    container_name: lidarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - ~/storage/lidarr/config:/config
      - /mnt/storage-hdd/Media/Music:/music
      - /mnt/storage-hdd/Downloads:/downloads
    ports:
      - 8686:8686
    networks:
      - cheeselab
    restart: unless-stopped

networks:
  cheeselab:
    external: true
```

## Notes

- Access `lidarr` at [http://cheeselab:8686](http://cheeselab:8686) (Local Network Only)