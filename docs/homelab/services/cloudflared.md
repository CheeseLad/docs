# Cloudflared
    
    

## Description

Cloudflared is a proxy server from Cloudflare that helps secure and accelerate your homelab by sitting between your home network and the internet. Its main purpose is to protect your home server from outside attacks and improve performance by caching and compressing data. One of its useful features is the ability to expose your homelab services to the internet without having to open up ports on your router, making it a great option for those who want to access their servers remotely. Cloudflared also provides features like encryption, firewall rules, and intrusion detection to keep your homelab safe and secure.

## Docker Compose File

```yaml
services:
  cloudflared:
    image: cloudflare/cloudflared
    container_name: cloudflared
    hostname: cloudflared
    restart: unless-stopped
    network_mode: "host"
    command: tunnel run
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - ~/storage/cloudflared/hosts:/etc/hosts
    environment:
      - "TUNNEL_TOKEN=${CLOUDFLARE_TUNNEL_TOKEN}"
```

## Notes

None