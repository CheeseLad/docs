# Tautulli
    
    

## Description

Tautulli is a popular monitoring and analytics tool for Plex media servers, providing insights into your media consumption habits and server performance. Its purpose is to help you keep track of who's watching what, when, and where, making it a great tool for managing a shared media library. Tautulli offers features like user tracking, playback statistics, and notifications, giving you a better understanding of your Plex usage. With its user-friendly interface and customizable dashboards, Tautulli makes it easy to stay on top of your media server's activity.

## Docker Compose File

```yaml
services:
  tautulli:
    container_name: tautulli
    image: tautulli/tautulli
    restart: unless-stopped
    volumes:
      - ~/storage/tautulli:/config
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    ports:
      - 8181:8181
    networks:
      - cheeselab

networks:
  cheeselab:
    external: true
```

## Notes

- Access `tautulli` at [http://cheeselab:8181](http://cheeselab:8181) (Local Network Only)