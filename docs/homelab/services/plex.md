# Plex
    
    

## Description

Plex is a popular media server that allows you to organize and stream your personal media collection, including movies, TV shows, and music, to various devices. Its purpose is to provide a centralized hub for all your media, making it easily accessible and playable on devices like smart TVs, smartphones, and gaming consoles. Plex also offers useful features like automatic content organization, metadata tagging, and live TV streaming, making it a great option for home entertainment. With Plex, you can enjoy your favorite media from anywhere, at any time, with a user-friendly interface and robust features.

## Docker Compose File

```yaml
services:
  plex:
    image: plexinc/pms-docker:public
    container_name: plex
    restart: unless-stopped
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
      - ~/storage/plex:/config
      - /mnt/storage-hdd/Media:/media
      - /dev/shm:/transcode
    environment:
      TZ: $TZ
      HOSTNAME: "dockerPlex"
      PLEX_UID: $PUID
      PLEX_GID: $PGID
      ADVERTISE_IP: http://$SERVER_IP:32400/
      ALLOWED_NETWORKS: $LOCAL_NETWORK
    networks:
      - cheeselab

networks:
  cheeselab:
    external: true
```

## Notes

- Access `plex` at [http://cheeselab:32400](http://cheeselab:32400) (Local Network Only)