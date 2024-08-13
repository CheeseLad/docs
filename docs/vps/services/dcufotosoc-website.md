# DCU Fotosoc Website

## Description

*Full Stack Website Built For DCU Fotosoc - DCU's Photography Society (Website currently in development)*

### Tech Stack Used:
- React
- TailwindCSS
- Firebase
- MongoDB, Express (Deprecated)
- Nginx
- Docker
- [Clubs & Socs API](https://github.com/CheeseLad/clubsandsocs-api)
- Stripe API

### Website Content & Features:
- Society information, contact details & social media accounts list
- User auth, account creation for members to make their own personal photography portfolio
- Easily update the website's gallery using a form that is restricted to specific users
- Store page powered by the Stripe API to allow members to purchase merch and photo books
- Automated event information from my custom [Clubs & Socs API](https://github.com/CheeseLad/clubsandsocs-api) 
- Testimonials from members and photo of the week display
- View the slides from previous Fotosoc workshops
- Meet the committee page with committee history and contact information

## Docker Compose File

```yaml
services:
  dcufotosoc-website:
    image: ghcr.io/cheeselad/fotosoc:latest
    container_name: dcufotosoc-website
    hostname: dcufotosoc-website
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.dcufotosoc-website.entrypoints=https"
      - "traefik.http.routers.dcufotosoc-website.rule=Host(`dcufotosoc.jakefarrell.ie`)"
    volumes:
      - ./env-config.js:/usr/share/nginx/html/env-config.js


networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access the DCU Fotosoc website here: [`https://dcufotosoc.jakefarrell.ie`](https://dcufotosoc.jakefarrell.ie)