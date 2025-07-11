# Pi Hole
    
    

## Description

Pi Hole is a network-wide ad blocker that runs on a Raspberry Pi or other devices, acting as a DNS server to filter out unwanted ads and trackers. Its main purpose is to improve browsing experience and reduce distractions, while also helping to block malicious websites and protect your network from malware. Pi Hole is highly customizable, allowing users to add or remove blocklists, whitelist specific sites, and even monitor DNS queries. By running Pi Hole, you can enjoy a faster and more secure internet experience across all devices connected to your network.

## Docker Compose File

```yaml
services:
  pihole:
    container_name: pihole
    hostname: pihole
    image: pihole/pihole:latest
    ports:
      - "3002:80/tcp"
      - "53:53/tcp"
      - "53:53/udp"
      - "67:67/udp"
    environment:
      TZ: 'Europe/Dublin'
      PIHOLE_DNS_: '8.8.8.8;8.8.4.4'
      WEBTHEME: 'default-darker'
    volumes:
      - '~/storage/pi-hole/etc-pihole:/etc/pihole'
      - '~/storage/pi-hole/etc-dnsmasq.d:/etc/dnsmasq.d'
    cap_add:
      - NET_ADMIN
    restart: unless-stopped
    env_file:
     - path: /home/jake/services/pi-hole/.env
```

## Notes

- Access `pihole` at [http://cheeselab:3002](http://cheeselab:3002) (Local Network Only)