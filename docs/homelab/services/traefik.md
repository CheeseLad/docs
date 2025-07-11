# Traefik
    
    

## Description

Traefik is a popular, open-source reverse proxy and load balancer that helps manage and route traffic to your homelab services. Its purpose is to simplify the process of exposing your services to the internet while providing features like SSL encryption, authentication, and routing rules. With Traefik, you can easily manage multiple services and domains from a single interface, making it a great addition to any homelab setup. It also supports automated SSL certificate management through services like Let's Encrypt, making it easy to secure your services.

## Docker Compose File

```yaml
services:
  traefik:
    image: traefik:v3.4
    container_name: traefik
    ports:
      - "8080:8080"
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./traefik.yml:/etc/traefik/traefik.yml:ro
    networks:
      - traefik
    restart: unless-stopped

networks:
  traefik:
    external: true
```

## Notes

- Access `traefik` at [http://cheeselab:8080](http://cheeselab:8080) (Local Network Only)