# Paperless Ngx
    
    

## Description

Paperless Ngx is a homelab service that helps you manage and digitize your documents, allowing you to store and organize your papers electronically. Its purpose is to make it easy to scan, index, and search your documents, freeing up physical storage space and making them more accessible. With features like automatic document recognition, tagging, and full-text search, Paperless Ngx simplifies the process of going paperless. This service is particularly useful for keeping track of receipts, invoices, and other important papers in a clutter-free and easily searchable way.

## Docker Compose File

```yaml
services:
  broker:
    image: docker.io/library/redis:7
    restart: unless-stopped
    volumes:
      - redisdata:/data

  paperless-ngx:
    image: ghcr.io/paperless-ngx/paperless-ngx:latest
    restart: unless-stopped
    container_name: paperless-ngx
    depends_on:
      - broker
    ports:
      - "8545:8000"
    volumes:
      - ~/storage/paperless-ngx/config/data:/usr/src/paperless/data
      - ~/storage/paperless-ngx/config/media:/usr/src/paperless/media
      - ~/storage/paperless-ngx/config/export:/usr/src/paperless/export
      - ~/storage/paperless-ngx/config/consume:/usr/src/paperless/consume
    env_file: .env
    environment:
      PAPERLESS_REDIS: redis://broker:6379

volumes:
  data:
  media:
  redisdata:
```

## Notes

- Access `paperless-ngx` at [http://cheeselab:8545](http://cheeselab:8545) (Local Network Only)