# Cable Network Website Backend
    
    

## Description

Founded in 2020, Cable Creative Roleplay has been the go-to place for fans of creative roleplay. We offer an experience like no other, with multiple different roleplay opportunities available to you. You can play around with plugins such as Crypto & Garages, and also get involved with the community by joining some of the many groups we have on offer. Come join us to find out more!

## Docker Compose File

```yaml
services:
  cablenetwork-website-backend:
    image: ghcr.io/cheeselad/cablenetwork-website-backend-api:latest
    container_name: cablenetwork-website-backend
    hostname: cablenetwork-website-backend
    restart: unless-stopped
    environment:
      - STEAM_API_KEY=${STEAM_API_KEY}
      - STEAM_WORKSHOP_COLLECTION_ID=${STEAM_WORKSHOP_COLLECTION_ID}
      - UNTURNED_SERVER_DATABASE_HOST=${UNTURNED_SERVER_DATABASE_HOST}
      - UNTURNED_SERVER_DATABASE_USER=${UNTURNED_SERVER_DATABASE_USER}
      - UNTURNED_SERVER_DATABASE_PASSWORD=${UNTURNED_SERVER_DATABASE_PASSWORD}
      - UNTURNED_SERVER_DATABASE_NAME=${UNTURNED_SERVER_DATABASE_NAME}
      - UNTURNED_API_KEY=${UNTURNED_API_KEY}
      - SERVER_ID=${SERVER_ID}
      - APP_URL="https://api.cablenetwork.xyz"
    networks:
      - cheeselab
    ports:
      - "6023:5000"

networks:
  cheeselab:
    external: true
```

## Notes

- Access `cablenetwork-website-backend` at [https://api.cablenetwork.xyz](https://api.cablenetwork.xyz) (Publicly Accessible)