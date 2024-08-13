# DCU Media Production Society Website

## Description

*Full Stack Website Built For DCU Media Production Society*

### Tech Stack Used:
- Django
- Python
- Bootstrap
- JavaScript
- SQLite
- Docker
- [Clubs & Socs API](https://github.com/CheeseLad/clubsandsocs-api)
- WordPress REST API

### Website Content & Features:
- Society information, contact details & social media accounts list
- Preview of latest articles from [thecollegeview.ie](https://thecollegeview.ie) using the WordPress REST API
- Blog system containing 2018-2021 blogs imported from Squarespace with sharing options
- Automated event information from my custom [Clubs & Socs API](https://github.com/CheeseLad/clubsandsocs-api) 
- Automated querying of YouTube videos
- Twitch stream with automated radio show timetable
- Sponsor list & testimonials
- Meet the committee page with committee video, committee history and contact information

## Docker Compose File

```yaml
services:
  dcumps-website:
    image: ghcr.io/dcumps/dcumps-website-django:latest
    container_name: dcumps-website
    hostname: dcumps-website
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.dcumps-website.entrypoints=https"
      - "traefik.http.routers.dcumps-website.rule=Host(`www.dcumps.ie`)"
      - "traefik.http.routers.dcumps-website.tls.certresolver=dcumps"
      - "traefik.http.routers.dcumps-website-base-url.entrypoints=https"
      - "traefik.http.routers.dcumps-website-base-url.rule=Host(`dcumps.ie`)"
      - "traefik.http.routers.dcumps-website-base-url.tls.certresolver=dcumps"

networks:
  default:
    external:
      name: traefik_net
```

## Notes

- Access the DCU Media Production Society website here: [`https://dcumps.ie`](https://dcumps.ie)