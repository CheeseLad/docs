# Navidrome
    
    

## Description

Navidrome is a free, open-source music server that allows you to stream your music collection to various devices. Its main purpose is to provide a self-hosted alternative to popular music streaming services, giving you full control over your music library. Navidrome features support for multiple formats, playlists, and album art, as well as apps for Android and iOS devices. With Navidrome, you can access your music from anywhere, without relying on third-party services or subscriptions.

## Docker Compose File

```yaml
services:
  navidrome:
    image: deluan/navidrome:latest
    container_name: navidrome
    user: 1000:1000 # should be owner of volumes
    ports:
      - "4533:4533"
    environment:
      # Optional: put your config options customization here. Examples:
      ND_LOGLEVEL: info
      ND_ENABLESUBSONIC: true
    volumes:
      - ~/storage/navidrome:/data
      - /mnt/storage-hdd/Media/Music:/music:ro
    networks:
      - cheeselab
    restart: unless-stopped

networks:
  cheeselab:
    external: true

```

## Notes

- Access `navidrome` at [http://cheeselab:4533](http://cheeselab:4533) (Local Network Only)