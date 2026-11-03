# Zipline
    
    

## Description

Zipline is a lightweight self‑hosted file‑sharing hub you can run in a Docker container (e.g. ghcr.io/diced/zipline:3.7.10). It gives you a quick, password‑protected web UI to drop files, generate temporary links, and even set expiration times—perfect for swapping big media or backups between devices on your LAN. The service supports chunked uploads, configurable storage paths, and optional encryption, so you keep everything private without needing a full‑blown cloud provider. Just spin it up, point a browser at the port, and start zipping files back and forth.

## Docker Compose File

```yaml
services:
  zipline-postgres:
    image: postgres:15
    restart: unless-stopped
    container_name: "zipline-postgres"
    environment:
      - POSTGRES_USER=$POSTGRES_USER
      - POSTGRES_PASSWORD=$POSTGRES_PASSWORD
      - POSTGRES_DB=$POSTGRES_DATABASE
    networks:
      - cheeselab
    volumes:
      - ~/storage/zipline/pg_data:/var/lib/postgresql/data
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U postgres']
      interval: 10s
      timeout: 5s
      retries: 5

  zipline:
    image: ghcr.io/diced/zipline:3.7.10
    restart: unless-stopped
    container_name: zipline
    ports:
      - "5000:5000"
    networks:
      - cheeselab
    environment:
      - CORE_RETURN_HTTPS=false
      - CORE_SECRET=$CORE_SECRET
      - CORE_HOST=0.0.0.0
      - CORE_PORT=5000
      - CORE_DATABASE_URL=$CORE_DATABASE_URL
      - CORE_LOGGER=true
    volumes:
      - '~/storage/zipline/uploads:/zipline/uploads'
      - '~/storage/zipline/public:/zipline/public'
    depends_on:
      - 'zipline-postgres'
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.zipline.entrypoints=https"
      - "traefik.http.routers.zipline.rule=Host(`i.jakefarrell.ie`)"

volumes:
  pg_data:

networks:
  cheeselab:
    external: true
```

## Notes

- Access `zipline` at [http://cheeselab:5000](http://cheeselab:5000) (Local Network Only)