# CollegeGuide
    
    

## Description

CollegeGuide is a web-based student companion platform designed to connect students across Ireland and make their college lives easier. Built with a "by students, for students" approach, it offers practical academic tools by combining on-demand chatbot support with rich, community-driven interactions through dedicated module-based discussion boards.

## Docker Compose File

```yaml
services:
  collegeguide-backend:
    container_name: collegeguide-backend
    hostname: collegeguide-backend
    image: ghcr.io/cheeselad/collegeguide-gh-backend:latest
    restart: unless-stopped
    ports:
      - "8000:8000"
    environment:
      - AI_API_KEY=$AI_API_KEY
      - SECRET_KEY=$SECRET_KEY
      - DEBUG=$DEBUG
      - EMAIL_HOST_PASSWORD=$EMAIL_HOST_PASSWORD
      - BASE_URL=$BASE_URL
    depends_on:
      - collegeguide-redis
    network_mode: "host"
    command: >
      sh -c "(python manage.py runserver 0.0.0.0:8000 &) &&
      celery -A collegeguide beat"

  collegeguide-frontend:
    container_name: collegeguide-frontend
    hostname: collegeguide-frontend
    image: ghcr.io/cheeselad/collegeguide-gh-frontend:latest
    restart: unless-stopped
    ports:
      - "5173:5173"
    environment:
      - VITE_API_URL=https://collegeguide-api.jakefarrell.ie
    depends_on:
      - collegeguide-backend
    networks:
      - collegeguide-network

  collegeguide-blog:
    container_name: collegeguide-blog
    hostname: collegeguide-blog
    image: ghcr.io/cheeselad/collegeguide-gh-blog:latest
    restart: unless-stopped
    ports:
      - "1313:80"
    environment:
      - APP_URL="https://collegeguide-blog.jakefarrell.ie"
    networks:
      - collegeguide-network

  collegeguide-redis:
    image: redis:6.2-alpine
    container_name: collegeguide-redis
    hostname: collegeguide-redis
    restart: unless-stopped
    ports:
      - '6379:6379'
    command: redis-server --save 20 1 --loglevel warning
    volumes: 
      - cache:/data
    network_mode: "host"

volumes:
  cache:
    driver: local

networks:
  collegeguide-network:
    driver: bridge
```

## Notes

- Access `collegeguide-backend` at [https://collegeguide-api.jakefarrell.ie](https://collegeguide-api.jakefarrell.ie) (Publicly Accessible)
- Access `collegeguide-frontend` at [https://collegeguide.jakefarrell.ie](https://collegeguide.jakefarrell.ie) (Publicly Accessible)
- Access `collegeguide-blog` at [https://collegeguide-blog.jakefarrell.ie](https://collegeguide-blog.jakefarrell.ie) (Publicly Accessible)