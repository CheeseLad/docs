# CA298 University System
    
    

## Description

CA298 Project 2: React Frontend University System: Grade 100%

## Docker Compose File

```yaml
services:
  ca298-universitysystem-frontend:
    image: ghcr.io/cheeselad/ca298-universitysystem-frontend:latest
    container_name: ca298-universitysystem-frontend
    hostname: ca298-universitysystem-frontend
    restart: unless-stopped
    ports:
      - "3014:80"
    networks:
      - ca298-universitysystem-network
    depends_on:
      - ca298-universitysystem-backend
    environment:
      - REACT_APP_API_URL=https://universitysystem-api.jakefarrell.ie

  ca298-universitysystem-backend:
    image: ghcr.io/cheeselad/ca298-universitysystem-backend:latest
    container_name: ca298-universitysystem-backend
    hostname: ca298-universitysystem-backend
    restart: unless-stopped
    ports:
      - "3015:8000"
    networks:
      - ca298-universitysystem-network

networks:
  ca298-universitysystem-network:
    driver: bridge
```

## Notes

- Access `ca298-universitysystem-frontend` at [https://universitysystem.jakefarrell.ie](https://universitysystem.jakefarrell.ie) (Publicly Accessible)
- Access `ca298-universitysystem-backend` at [https://universitysystem-api.jakefarrell.ie](https://universitysystem-api.jakefarrell.ie) (Publicly Accessible)