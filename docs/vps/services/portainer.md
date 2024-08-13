# Portainer

## Docker Compose File

```yaml
services:
  portainer:
    container_name: portainer
    hostname: portainer
    image: portainer/portainer-ce:latest
    volumes:
      - ./data:/data
      - /var/run/docker.sock:/var/run/docker.sock
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.portainer.rule=Host(`portainer.jakefarrell.ie`)"
      - "traefik.http.routers.portainer.entrypoints=https"
      - "traefik.http.services.portainer.loadbalancer.server.port=9000"
      - "traefik.http.routers.portainer.service=portainer"
    
volumes:
  data:

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access Portainer here: [`https://portainer.jakefarrell.ie`](https://portainer.jakefarrell.ie)