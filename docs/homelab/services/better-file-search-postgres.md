# Better File Search Postgres
    
    

## Description

Specific PGVector version used for the development of Better File Search.

## Docker Compose File

```yaml
services:
  better-file-search-postgres:
    image: pgvector/pgvector:0.8.1-pg18-trixie
    container_name: better-file-search-postgres
    restart: unless-stopped
    ports:
      - "54346:5432"
    environment:
      POSTGRES_DB: better_file_search_db
      POSTGRES_USER: bfs
      POSTGRES_PASSWORD: pass
    volumes:
      - bfs_pgdata_jake:/var/lib/postgresql

volumes:
  bfs_pgdata_jake:

```

## Notes

None