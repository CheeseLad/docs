# Portainer


## Docker Compose File

```yaml
version: "3"
services:
  portainer:
    container_name: portainer
    hostname: portainer
    image: portainer/portainer-ce:latest
    ports:
      - 9443:9443
    volumes:
      - ./config/data:/data
      - /var/run/docker.sock:/var/run/docker.sock
    restart: unless-stopped
    
volumes:
  data:
```

## Notes

- Access Portainer at `https://192.168.1.3:9443` (Local Network Only)
- Web UI only works with HTTPS, so you need to use `https://` instead of `http://`, certificate is not required.