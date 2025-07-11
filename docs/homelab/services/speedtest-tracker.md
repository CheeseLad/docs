# Speedtest Tracker
    
    

## Description

Speedtest Tracker is a homelab service that monitors and tracks your internet speed over time, providing valuable insights into your network's performance. Its purpose is to help you identify any issues or fluctuations in your internet connection, allowing you to troubleshoot or contact your ISP for support. The service often includes features like automatic speed testing, historical data graphs, and alerts for when your speed drops below a certain threshold. By using Speedtest Tracker, you can ensure you're getting the internet speeds you're paying for and optimize your online experience.

## Docker Compose File

```yaml
services:
    speedtest-tracker:
        image: lscr.io/linuxserver/speedtest-tracker:latest
        restart: unless-stopped
        container_name: speedtest-tracker
        ports:
            - 8765:80
        environment:
            - PUID=1000
            - PGID=1000
            - APP_KEY=${APP_KEY}
            - DB_CONNECTION=sqlite
            - APP_NAME="CheeseLab Speedtest Tracker"
            - APP_URL="https://speedtest.jakefarrell.ie"
            - ASSET_URL="https://speedtest.jakefarrell.ie"
            - APP_TIMEZONE=Europe/Dublin
            - SPEEDTEST_SCHEDULE="0 * * * *"
        volumes:
            - ~/storage/speedtest-tracker/new-config:/config
```

## Notes

- Access `speedtest-tracker` at [https://speedtest.jakefarrell.ie](https://speedtest.jakefarrell.ie) (Publicly Accessible)