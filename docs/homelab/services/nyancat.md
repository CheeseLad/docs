# Nyan Cat
    
    

## Description

Nyan Cat made with HTML5+CSS3+JavaScript hosted on an Nginx server in a Docker container.

Source Code: [GitHub Repository](https://github.com/cristurm/nyan-cat)

## Docker Compose File

```yaml
services:
  nyancat:
    image: nginx:latest
    container_name: nyancat
    restart: unless-stopped
    volumes:
      - ~/storage/nyancat:/usr/share/nginx/html
    ports:
      - "3022:80"
    networks:
      - cheeselab

networks:
  cheeselab:
    external: true
```

## Notes

- Access `nyancat` at [https://nyancat.jakefarrell.ie](https://nyancat.jakefarrell.ie) (Publicly Accessible)