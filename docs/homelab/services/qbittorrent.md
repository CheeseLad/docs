# Qbittorrent

## Description

Qbittorrent is a free, open-source, and cross-platform BitTorrent client. It is lightweight, fast, and easy to use. Qbittorrent is available for Windows, macOS, Linux, OS/2, and FreeBSD.

## Docker Compose File

```yaml
services:
  qbittorrent:
    image: lscr.io/linuxserver/qbittorrent:4.6.0
    container_name: qbittorrent
    hostname: qbittorrent
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - WEBUI_PORT=3001
      - TORRENTING_PORT=6881
    volumes:
      - ~/storage/qbittorrent:/config
      - ~/downloads/qbittorrent:/downloads
    ports:
      - 3001:3001
      - 6881:6881
      - 6881:6881/udp
    restart: unless-stopped
```

## Notes

- Access Qbittorrent at `http://cheeselab:3001` (Local Network Only)