# DCUfotosoc Website
    
    

## Description

*Full Stack Website Built For DCU Fotosoc - DCU's Photography Society*

Tech Stack Used:
- React
- TailwindCSS
- Firebase
- Nginx
- Docker
- [Clubs & Socs API](https://github.com/CheeseLad/clubsandsocs-api)

Website Content & Features:
- Society information, contact details & social media accounts list
- User auth, account creation for members to make their own personal photography portfolio
- Easily update the website's gallery using a form that is restricted to specific users
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
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.dcufotosoc-website-jf.entrypoints=https"
      - "traefik.http.routers.dcufotosoc-website-jf.rule=Host(`dcufotosoc.jakefarrell.ie`)"
      - "traefik.http.routers.dcufotosoc-website.entrypoints=https"
      - "traefik.http.routers.dcufotosoc-website.rule=Host(`www.dcufotosoc.ie`)"
      - "traefik.http.routers.dcufotosoc-website.tls.certresolver=dcufotosoc"
      - "traefik.http.routers.dcufotosoc-website-base-url.entrypoints=https"
      - "traefik.http.routers.dcufotosoc-website-base-url.rule=Host(`dcufotosoc.ie`)"
      - "traefik.http.routers.dcufotosoc-website-base-url.tls.certresolver=dcufotosoc"
    environment:
      - REACT_APP_STRIPE_PUBLISHABLE_KEY=${REACT_APP_STRIPE_PUBLISHABLE_KEY}
      - REACT_APP_STRIPE_PRICE_ID=${REACT_APP_STRIPE_PRICE_ID}
      - REACT_APP_ADMIN_USER_ID=${REACT_APP_ADMIN_USER_ID}
      - REACT_APP_FIREBASE_API_KEY=${REACT_APP_FIREBASE_API_KEY}
      - REACT_APP_FIREBASE_AUTH_DOMAIN=${REACT_APP_FIREBASE_AUTH_DOMAIN}
      - REACT_APP_FIREBASE_PROJECT_ID=${REACT_APP_FIREBASE_PROJECT_ID}
      - REACT_APP_FIREBASE_STORAGE_BUCKET=${REACT_APP_FIREBASE_STORAGE_BUCKET}
      - REACT_APP_FIREBASE_MESSAGING_SENDER_ID=${REACT_APP_FIREBASE_MESSAGING_SENDER_ID}
      - REACT_APP_FIREBASE_APP_ID=${REACT_APP_FIREBASE_APP_ID}
      - REACT_APP_BACKEND_API_URL=${REACT_APP_BACKEND_API_URL}

  dcufotosoc-backend:
    image: ghcr.io/cheeselad/fotosoc-backend:latest
    container_name: dcufotosoc-backend
    restart: unless-stopped
    expose:
      - "5000"
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.dcufotosoc-backend.entrypoints=https"
      - "traefik.http.routers.dcufotosoc-backend.rule=Host(`api.dcufotosoc.ie`)"
      - "traefik.http.routers.dcufotosoc-backend.tls.certresolver=dcufotosoc"
      - "traefik.http.services.dcufotosoc-backend.loadbalancer.server.port=5000"
    environment:
      - MAIL_PASSWORD=${MAIL_PASSWORD}
      - MAIL_USERNAME=${MAIL_USERNAME}
      - MAIL_DEFAULT_SENDER=${MAIL_DEFAULT_SENDER}
      - MAIL_REPLY_TO=${MAIL_REPLY_TO}
      - SHEET_ID=${SHEET_ID}
      - CALENDAR_ID=${CALENDAR_ID}
    volumes:
      - "./credentials.json:/app/credentials.json:ro"

networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access `dcufotosoc-website` at [https://dcufotosoc.jakefarrell.ie](https://dcufotosoc.jakefarrell.ie) (Publicly Accessible via Traefik)
- Access `dcufotosoc-website` at [https://www.dcufotosoc.ie](https://www.dcufotosoc.ie) (Publicly Accessible via Traefik)
- Access `dcufotosoc-website` at [https://dcufotosoc.ie](https://dcufotosoc.ie) (Publicly Accessible via Traefik)
- Access `dcufotosoc-backend` at [https://api.dcufotosoc.ie](https://api.dcufotosoc.ie) (Publicly Accessible via Traefik)