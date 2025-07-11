# Portainer
    
    

## Description

Portainer is a popular, open-source management platform for Docker, making it easy to manage and monitor your containers, images, and volumes. Its purpose is to simplify the process of deploying and managing containerized applications, making it a great tool for home servers and homelabs. With Portainer, you can easily create, manage, and troubleshoot your containers, as well as access features like templates, backups, and user management. It provides a user-friendly web interface that's perfect for those who want to manage their Docker environment without using the command line.

## Docker Compose File

```yaml
services:
  portainer:
    container_name: portainer
    hostname: portainer
    image: portainer/portainer-ce:latest
    ports:
      - 9443:9443
    volumes:
      - ~/storage/portainer:/data
      - /var/run/docker.sock:/var/run/docker.sock
    restart: unless-stopped
    
volumes:
  data:
```

## Notes

- Access `portainer` at [https://cheeselab:9443](https://cheeselab:9443) (Local Network Only)