# DDClient
    
    

## Description

DDClient is a lightweight, open-source service that updates DNS records in real-time, allowing users to access their home server or other devices remotely. Its purpose is to provide a dynamic DNS (DDNS) solution, which is useful for users with dynamic IP addresses that change periodically. DDClient supports a wide range of dynamic DNS providers, making it easy to set up and use. By using ddclient, users can access their home server or other devices from anywhere, without needing to know the current IP address.

## Docker Compose File

```yaml
services:
  ddclient:
    image: lscr.io/linuxserver/ddclient:latest
    container_name: ddclient
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - ~/storage/ddclient:/config
    restart: unless-stopped
```

## Notes

None