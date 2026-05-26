# Openspeedtest
    
    

## Description

Openspeedtest is a self-hosted speed test solution that allows you to measure your internet bandwidth from within your own network. Its purpose is to provide an accurate and unbiased measure of your internet speed, without relying on third-party services. This service is useful for homelab setups where you want to monitor and troubleshoot your network performance without relying on external speed test websites. By hosting it yourself, you can also avoid any potential limitations or biases that might come with using a public speed test service.

## Docker Compose File

```yaml
services:
    openspeedtest:
       restart: unless-stopped
       container_name: openspeedtest
       ports:
            - '3604:3000'
            - '3605:3001'
       image: openspeedtest/latest
       networks:
        - cheeselab

networks:
  cheeselab:
    external: true
```

## Notes

- Access `openspeedtest` at [http://cheeselab:3604](http://cheeselab:3604) (Local Network Only)