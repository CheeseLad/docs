# Uptime Kuma
    
    

## Description

Uptime Kuma is a self-hosted monitoring tool that helps you keep track of your websites, servers, and other services' uptime and downtime. Its purpose is to send notifications when something goes wrong, so you can quickly act and minimize losses. Uptime Kuma is known for its ease of use, customizable alerts, and detailed reporting features. It's a great addition to any homelab, allowing you to monitor your services from a single, user-friendly dashboard.

## Docker Compose File

```yaml
services:
  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    volumes:
      - ~/storage/uptime-kuma:/app/data
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - APP_URL="https://status.jakefarrell.ie"
    ports:
      - 3003:3001
    restart: unless-stopped
```

## Notes

- Access `uptime-kuma` at [https://status.jakefarrell.ie](https://status.jakefarrell.ie) (Publicly Accessible)