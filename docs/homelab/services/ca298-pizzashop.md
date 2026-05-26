# CA298 PizzaShop
    
    

## Description

CA298 Full Stack Development Project 1: Django Frontend & Backend: Grade 100%

## Docker Compose File

```yaml
services:
  ca298-pizzashop:
    image: ghcr.io/cheeselad/ca298-pizzashop:latest
    container_name: ca298-pizzashop
    restart: unless-stopped
    volumes:
      - ~/storage/ca298-pizzashop/db.sqlite3:/app/pizzashop/db.sqlite3
    ports:
      - "3021:8000"
    networks:
      - cheeselab

networks:
  cheeselab:
    external: true
```

## Notes

- Access `ca298-pizzashop` at [https://pizzashop.jakefarrell.ie](https://pizzashop.jakefarrell.ie) (Publicly Accessible)