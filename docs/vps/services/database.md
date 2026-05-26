# Database
    
    

## Description

MySQL database used for multiple services that require a database.

## Docker Compose File

```yaml
services:
  database:
    image: mysql:8.3.0
    container_name: database
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
  data:
    driver: local
  logs:
    driver: local

```

## Notes

None