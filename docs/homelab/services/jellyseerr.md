# Jellyseerr
    
    

## Description

Jellyseerr is a personalized media management service that helps users manage and stream their media collections. Its purpose is to provide a simple and easy-to-use interface for organizing and accessing movies, TV shows, and other media content. Jellyseerr offers features like automated metadata tagging, media organization, and streaming capabilities, making it a great addition to any homelab setup. By integrating with other services, Jellyseerr allows users to easily find and watch their favorite media content from a single, convenient interface.

## Docker Compose File

```yaml
services:
  jellyseerr:
    image: fallenbagel/jellyseerr:latest
    container_name: jellyseerr
    environment:
      - LOG_LEVEL=debug
      - TZ=Europe/Dublin
      - PORT=5057 #optional
    ports:
      - 5057:5057
    volumes:
      - ~/storage/jellyseerr/config:/app/config
    networks:
      - cheeselab
    restart: unless-stopped

networks:
  cheeselab:
    external: true
```

## Notes

- Access `jellyseerr` at [http://cheeselab:5057](http://cheeselab:5057) (Local Network Only)