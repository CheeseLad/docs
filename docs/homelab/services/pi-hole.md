# Pi-hole

## Description

Pi-hole is a network-wide ad blocker. It blocks ads on any device and improves overall network performance.

## Docker Compose File

```yaml
services:
  pihole:
    container_name: pihole
    hostname: pihole
    image: pihole/pihole:latest
    ports:
      - "53:53/tcp"
      - "53:53/udp"
      - "67:67/udp"
      - "3002:80/tcp"
    environment:
      TZ: 'Europe/Dublin'
      PIHOLE_DNS_: '8.8.8.8;8.8.4.4'
      WEBTHEME: 'default-darker'
    volumes:
      - './etc-pihole:/etc/pihole'
      - './etc-dnsmasq.d:/etc/dnsmasq.d'
    cap_add:
      - NET_ADMIN
    restart: unless-stopped
    env_file:
     - path: /home/jake/services/pi-hole/.env

```

## Notes

- Access Pi-Hole at [http://cheeselab:3002/admin](http://cheeselab:3002/admin) (Local Network Only)
- Per device configuration required to use Pi-Hole as a DNS server as to make it optional for devices on the network.