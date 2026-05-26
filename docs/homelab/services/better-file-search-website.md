# Better File Search Website
    
    

## Description

This website allows you to download all the installer releases from different branches of our Final Year Project - Better File Search. It is built using Vite React for the frontend and Flask for the backend, and it interacts with the Google Drive API to fetch the relevant files.

## Docker Compose File

```yaml
services:
  better-file-search-website-frontend:
    image: ghcr.io/cheeselad/better-file-search-website-frontend:latest
    container_name: better-file-search-website-frontend
    restart: unless-stopped
    ports:
      - "3024:80"
    networks:
      - cheeselab
  better-file-search-website-backend:
    image: ghcr.io/cheeselad/better-file-search-website-backend:latest
    container_name: better-file-search-website-backend
    restart: unless-stopped
    ports:
      - "3025:5000"
    environment:
      - ROOT_FOLDER_ID=${ROOT_FOLDER_ID}
    volumes:
      - ./better-file-search-sa.json:/app/better-file-search-sa.json:ro
    networks:
      - cheeselab

networks:
  cheeselab:
    external: true

```

## Notes

- Access `better-file-search-website-frontend` at [https://betterfilesearch.jakefarrell.ie](https://betterfilesearch.jakefarrell.ie) (Publicly Accessible)
- Access `better-file-search-website-backend` at [https://betterfilesearch-api.jakefarrell.ie](https://betterfilesearch-api.jakefarrell.ie) (Publicly Accessible)