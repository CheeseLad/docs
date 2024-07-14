# Tautulli

## Description

Tautulli is a monitoring and tracking tool for Plex Media Server. It tracks statistics like play counts, watched status, and more. It also provides notifications for new content and user activity.

## Docker Compose File

```yaml
services:
  tautulli:
    container_name: tautulli
    hostname: tautulli
    image: tautulli/tautulli
    restart: unless-stopped
    volumes:
      - /home/jake/services/tautulli/config:/config
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    ports:
      - 8181:8181
```

## Notes

- Access Tautulli at `http://cheeselab:8181` (Local Network Only)