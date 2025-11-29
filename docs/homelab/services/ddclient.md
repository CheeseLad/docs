# DDClient
    
    

## Description

DDClient is a lightweight, open-source Dynamic DNS (DDNS) update client that runs on your home server or homelab, designed to update your DNS records when your IP address changes. Its main purpose is to keep your remote access stable, allowing you to access your server from outside your network without worrying about IP address changes. The LinuxServer.io image provides an easy-to-use implementation of DDClient, supporting a wide range of DDNS providers. With DDClient, you can enjoy seamless remote access to your home server, even when your ISP assigns a new IP address to your connection.

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