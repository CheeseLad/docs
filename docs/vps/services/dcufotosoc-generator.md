# DCUfotosoc Generator
    
    

## Description

DCU Fotosoc Newsletter Generator is a web application that allows users to create newsletters for the DCU Photography Society. The application provides an interface for designing newsletters and adding content. It is built using modern web technologies and is designed to be user-friendly and efficient for creating professional-looking newsletters.

## Docker Compose File

```yaml
services:
  dcufotosoc-generator:
    image: ghcr.io/cheeselad/fotosoc-newsletter-generator-frontend:latest
    container_name: dcufotosoc-generator
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.dcufotosoc-generator.entrypoints=https"
      - "traefik.http.routers.dcufotosoc-generator.rule=Host(`generator.dcufotosoc.ie`)"
      - "traefik.http.routers.dcufotosoc-generator.tls.certresolver=dcufotosoc"
    environment:
      - VITE_API_URL=$VITE_API_URL
      - VITE_LISTMONK_MODE=$VITE_LISTMONK_MODE

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access `dcufotosoc-generator` at [https://generator.dcufotosoc.ie](https://generator.dcufotosoc.ie) (Publicly Accessible via Traefik)