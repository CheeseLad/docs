# Cable Network Website Frontend
    
    

## Description

Founded in 2020, Cable Creative Roleplay has been the go-to place for fans of creative roleplay. We offer an experience like no other, with multiple different roleplay opportunities available to you. You can play around with plugins such as Crypto & Garages, and also get involved with the community by joining some of the many groups we have on offer. Come join us to find out more!

## Docker Compose File

```yaml
services:
  cablenetwork-website-frontend:
    image: ghcr.io/cheeselad/cablenetwork-website-frontend:latest
    container_name: cablenetwork-website-frontend
    hostname: cablenetwork-website-frontend
    restart: unless-stopped
    networks:
      - cheeselab
    ports:
      - "6022:80"

networks:
  cheeselab:
    external: true
```

## Notes

- Access `cablenetwork-website-frontend` at [https://cablenetwork.jakefarrell.ie](https://cablenetwork.jakefarrell.ie) (Publicly Accessible)