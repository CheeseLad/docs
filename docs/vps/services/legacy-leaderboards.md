# Legacy Leaderboards
    
    

## Description

None

## Docker Compose File

```yaml
services:
  legacy-leaderboards:
    image: ghcr.io/cheeselad/legacy-leaderboards:latest
    container_name: legacy-leaderboards
    ports:
      - "8000:8000"
    environment:
      - SECRET_KEY=$SECRET_KEY
      - DEBUG=$DEBUG
      - ALLOWED_HOSTS=$ALLOWED_HOSTS
    volumes:
      - ~/storage/legacy-leaderboards/db.sqlite3:/app/db.sqlite3
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.legacy-leaderboards.entrypoints=https"
      - "traefik.http.routers.legacy-leaderboards.rule=Host(`legacyleaderboards.jakefarrell.ie`)"

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access `legacy-leaderboards` at [https://legacyleaderboards.jakefarrell.ie](https://legacyleaderboards.jakefarrell.ie) (Publicly Accessible via Traefik)