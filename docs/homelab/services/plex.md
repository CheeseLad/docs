# Plex

## Description

Plex is a media server that allows you to stream your media collection to any device. It is a powerful tool that can transcode media on-the-fly to ensure compatibility with any device.

## Docker Compose File

```yaml

networks:
  default:
    driver: bridge

services:
  plex:
    image: plexinc/pms-docker:public
    container_name: plex
    restart: unless-stopped
    networks:
      - default
    ports:
      - "32400:32400/tcp"
      - "3005:3005/tcp"
      - "8324:8324/tcp"
      - "32469:32469/tcp"
      - "1900:1900/udp"
      - "32410:32410/udp"
      - "32412:32412/udp"
      - "32413:32413/udp"
      - "32414:32414/udp"
    devices:
      - /dev/dri:/dev/dri
    volumes:
      - $DOCKERDIR/appdata/plex:/config
      - /mnt/usb1/Plex:/media
      - /mnt/usb2/Plex:/media2
      - /dev/shm:/transcode
    environment:
      TZ: $TZ
      HOSTNAME: "dockerPlex"
      PLEX_UID: $PUID
      PLEX_GID: $PGID
      ADVERTISE_IP: http://$SERVER_IP:32400/
      ALLOWED_NETWORKS: $LOCAL_NETWORK

```

## Notes

- Access Plex at `http://cheeselab:32400/web` (Local Network Only)