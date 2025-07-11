# Overseerr
    
    

## Description

Overseerr is a home server service that lets you request and manage media, like movies and TV shows, all in one place. Its main purpose is to make it easy for you and your family to find and watch your favorite shows without having to dig through different platforms. Overseerr integrates with other popular homelab services, allowing you to automate requests and get notified when your media is available. With Overseerr, you can also set up user profiles, track requests, and even get recommendations based on your viewing history.

## Docker Compose File

```yaml
services:
  overseerr:
    image: sctx/overseerr:latest
    container_name: overseerr
    environment:
      - LOG_LEVEL=debug
      - TZ=Europe/Dublin
      - PORT=5055
    ports:
      - 5055:5055
    volumes:
      - ~/storage/overseerr:/app/config
    networks:
      - cheeselab
    restart: unless-stopped

networks:
  cheeselab:
    external: true

```

## Notes

- Access `overseerr` at [http://cheeselab:5055](http://cheeselab:5055) (Local Network Only)