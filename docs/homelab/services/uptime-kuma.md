# Uptime Kuma

## Description

Uptime Kuma is a fancy self-hosted monitoring tool. It can monitor HTTP(s) and TCP endpoints, and can send notifications via Email, Discord, Slack, Telegram, and Webhooks. It also has a beautiful dashboard that can be customized to your liking.

## Docker Compose File

```yaml
services:
  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    hostname: uptime-kuma
    volumes:
      - ./uptime-kuma-data:/app/data
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - 3003:3001
    restart: unless-stopped
```

## Notes

- Access Uptime Kuma at [https://status.jakefarrell.ie](https://status.jakefarrell.ie)
- Login credentials required to access the dashboard
- Utilises Cloudflare Zero Trust for security and access control, allowing for secure access to Uptime Kuma from anywhere.