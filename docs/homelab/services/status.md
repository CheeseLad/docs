# Status
    
    

## Description

HTML file displaying "CheeseLab", used for pinging and health checks for the homelab.

## Docker Compose File

```yaml
services:
  status:
    image: nginx:latest
    container_name: status
    restart: unless-stopped
    volumes:
      - ~/storage/status:/usr/share/nginx/html
    ports:
      - "80:80"
    networks:
      - cheeselab

networks:
  cheeselab:
    external: true
```

## Notes

- Access `status` at [http://cheeselab:80](http://cheeselab:80) (Local Network Only)