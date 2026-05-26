# Plausible
    
    

## Description

Plausible Analytics gives you simple, privacy-friendly website analytics without cookies or personal data. It's trusted by thousands of subscribers as an alternative to Google Analytics that's easy to set up and understand. It's completely independent, self-funded and bootstrapped.

## Docker Compose File

```yaml
services:
  plausible_db:
    image: postgres:14-alpine
    restart: unless-stopped
    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=${PLAUSIBLE_DB_PASSWORD}

  plausible_events_db:
    image: clickhouse/clickhouse-server:24.3.3.102-alpine
    restart: unless-stopped
    volumes:
      - event-data:/var/lib/clickhouse
      - ./clickhouse-config.xml:/etc/clickhouse-server/config.d/logging.xml:ro
      - ./clickhouse-user-config.xml:/etc/clickhouse-server/users.d/logging.xml:ro
    ulimits:
      nofile:
        soft: 262144
        hard: 262144

  plausible:
    image: ghcr.io/plausible/community-edition:v2.1.1
    container_name: plausible
    restart: unless-stopped
    command: sh -c "sleep 10 && /entrypoint.sh db createdb && /entrypoint.sh db migrate && /entrypoint.sh run"
    depends_on:
      - plausible_db
      - plausible_events_db
    env_file:
      - plausible-conf.env
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.plausible.entrypoints=https"
      - "traefik.http.routers.plausible.rule=Host(`plausible.jakefarrell.ie`) || Host(`pa.jakefarrell.ie`)"
      - "traefik.http.services.plausible.loadbalancer.server.port=8000"

volumes:
  db-data:
    external: true
    name: hosting_db-data

  event-data:
    external: true
    name: hosting_event-data

networks:
  default:
    name: traefik_net
    external: true

```

## Notes

- Access `plausible` at [https://plausible.jakefarrell.ie](https://plausible.jakefarrell.ie) (Publicly Accessible via Traefik)