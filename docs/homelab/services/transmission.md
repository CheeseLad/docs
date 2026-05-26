# Transmission
    
    

## Description

Transmission is a popular open-source BitTorrent client that allows you to download and upload files using the BitTorrent protocol. Its main purpose is to provide a simple and efficient way to manage your torrent files, with features like download and upload speed limits, prioritization, and remote access. This containerized version from LinuxServer.io makes it easy to run Transmission on your home server or homelab, with a web-based interface for easy management. With Transmission, you can also set up automated downloads, streaming, and more, making it a versatile tool for your media needs.

## Docker Compose File

```yaml
---
services:
  transmission:
    image: lscr.io/linuxserver/transmission:latest
    container_name: transmission
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - TRANSMISSION_WEB_HOME= #optional
      - USER=${USER}
      - PASS=${PASS}
      - WHITELIST= #optional
      - PEERPORT= #optional
      - HOST_WHITELIST= #optional
    volumes:
      - ~/storage/transmission/config:/config
      - /mnt/storage-hdd/Downloads:/downloads
      - ~/storage/transmission/watch:/watch
    ports:
      - 9091:9091
      - 51413:51413
      - 51413:51413/udp
    networks:
      - cheeselab
    restart: unless-stopped

networks:
  cheeselab:
    external: true
```

## Notes

- Access `transmission` at [http://cheeselab:9091](http://cheeselab:9091) (Local Network Only)