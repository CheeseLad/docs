# DCU Clubs & Socs
    
    

## Description

None

## Docker Compose File

```yaml
services:
  dcuclubsandsocs:
    image: ghcr.io/cheeselad/dcuclubsandsocs:latest
    container_name: dcuclubsandsocs
    hostname: dcuclubsandsocs
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.dcuclubsandsocs.entrypoints=https"
      - "traefik.http.routers.dcuclubsandsocs.rule=Host(`dcuclubsandsocs.jakefarrell.ie`)"

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access `dcuclubsandsocs` at [https://dcuclubsandsocs.jakefarrell.ie](https://dcuclubsandsocs.jakefarrell.ie) (Publicly Accessible via Traefik)