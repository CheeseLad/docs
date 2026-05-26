# Listmonk
    
    

## Description

Listmonk is a self-hosted, open-source newsletter and mailing list manager that can be run on a VPS. Its purpose is to help users manage their email lists and send targeted campaigns to their subscribers. With features like automation, segmentation, and analytics, Listmonk provides a powerful platform for managing newsletters and email marketing efforts. By hosting Listmonk on a VPS, users can have full control over their data and mailing list management.

## Docker Compose File

```yaml
services:
  app:
    image: listmonk/listmonk:latest
    container_name: listmonk_app
    restart: unless-stopped
    networks:
      - traefik_net
      - listmonk
    depends_on:
      - db
    command: >
      sh -c "./listmonk --install --idempotent --yes --config '' &&
             ./listmonk --upgrade --yes --config '' &&
             ./listmonk --config ''"
    environment:
      LISTMONK_app__address: 0.0.0.0:9000
      LISTMONK_db__user: ${POSTGRES_USER}
      LISTMONK_db__password: ${POSTGRES_PASSWORD}
      LISTMONK_db__database: ${POSTGRES_DB}
      LISTMONK_db__host: listmonk_db
      LISTMONK_db__port: 5432
      LISTMONK_db__ssl_mode: disable
      LISTMONK_db__max_open: 25
      LISTMONK_db__max_idle: 25
      LISTMONK_db__max_lifetime: 300s
      TZ: Etc/UTC
      LISTMONK_ADMIN_USER: ${LISTMONK_ADMIN_USER:-}
      LISTMONK_ADMIN_PASSWORD: ${LISTMONK_ADMIN_PASSWORD:-}
    volumes:
      - ~/storage/listmonk/uploads:/listmonk/uploads:rw
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.listmonk.rule=Host(`lm.jakefarrell.ie`)"
      - "traefik.http.routers.listmonk.entrypoints=https"
      - "traefik.http.routers.listmonk.tls=true"
      - "traefik.http.routers.listmonk.tls.certresolver=cloudflare"
      - "traefik.http.services.listmonk.loadbalancer.server.port=9000"

  db:
    image: postgres:17-alpine
    container_name: listmonk_db
    restart: unless-stopped
    networks:
      - listmonk
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER}"]
      interval: 10s
      timeout: 5s
      retries: 6
    volumes:
      - listmonk-data:/var/lib/postgresql/data

networks:
  listmonk:
  traefik_net:
    external: true

volumes:
  listmonk-data:

```

## Notes

- Access `app` at [https://lm.jakefarrell.ie](https://lm.jakefarrell.ie) (Publicly Accessible via Traefik)