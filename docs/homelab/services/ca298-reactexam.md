# CA298 Reactexam
    
    

## Description

CA298 React Exam: React Frontend Shop System: Grade 100%

## Docker Compose File

```yaml
services:
  ca298-reactexam-frontend:
    image: ghcr.io/cheeselad/ca298-reactexam-frontend:latest
    container_name: ca298-reactexam-frontend
    hostname: ca298-reactexam-frontend
    restart: unless-stopped
    ports:
      - "3016:80"
    networks:
      - ca298-reactexam-network
    depends_on:
      - ca298-reactexam-backend
    environment:
      - REACT_APP_API_URL=https://reactexam-api.jakefarrell.ie

  ca298-reactexam-backend:
    image: ghcr.io/cheeselad/ca298-reactexam-backend:latest
    container_name: ca298-reactexam-backend
    hostname: ca298-reactexam-backend
    restart: unless-stopped
    ports:
      - "3017:8000"
    networks:
      - ca298-reactexam-network

networks:
  ca298-reactexam-network:
    driver: bridge
```

## Notes

- Access `ca298-reactexam-frontend` at [https://reactexam.jakefarrell.ie](https://reactexam.jakefarrell.ie) (Publicly Accessible)
- Access `ca298-reactexam-backend` at [https://reactexam-api.jakefarrell.ie](https://reactexam-api.jakefarrell.ie) (Publicly Accessible)