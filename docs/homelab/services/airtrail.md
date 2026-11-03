# Airtrail
    
    

## Description

Airtrail is a lightweight, self‑hosted flight‑tracking dashboard that pulls ADS‑B data and paints aircraft on an interactive map you can run right at home. It stores logs, lets you set up alerts or push data to MQTT, and even lets you tweak the map style or overlay your own layers. The whole thing spins up with a single `docker run johly/airtrail:latest` and drops you into a clean, web‑based UI. Perfect for hobbyists who want a private radar without signing up for a cloud service.

## Docker Compose File

```yaml
services:
  db:
    container_name: airtrail_db
    image: postgres:16-alpine
    restart: always
    env_file:
      - .env
    environment:
      POSTGRES_DB: ${DB_DATABASE_NAME}
      POSTGRES_USER: ${DB_USERNAME}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - db_data:/var/lib/postgresql/data
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U ${DB_USERNAME} -d ${DB_DATABASE_NAME}']
      interval: 5s
      timeout: 5s
      retries: 5
  airtrail:
    container_name: airtrail
    image: johly/airtrail:latest
    restart: always
    env_file:
      - .env
    ports:
      - 7482:3000
    volumes:
      # Required for file uploads (e.g., airline icons)
      # The path to the right of the colon needs to match UPLOAD_LOCATION in your .env file
      # AirTrail gives it to PUID:PGID (1000:1000 by default) on every start
      # - uploads:/app/uploads
      # To keep uploads in a folder on the host instead, use a bind mount, such as:
      - ~/storage/airtrail/uploads:/app/uploads
    depends_on:
      db:
        condition: service_healthy

volumes:
  db_data:
  uploads:

```

## Notes

- Access `airtrail` at [http://cheeselab:7482](http://cheeselab:7482) (Local Network Only)