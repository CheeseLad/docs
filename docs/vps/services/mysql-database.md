# MySQL Database

## Description

This service is used to host a MySQL database for various applications and services.

## Docker Compose File

```yaml
services:
  database:
    image: mysql:8.3.0
    hostname: database
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

```

## Notes

- Used across multiple containers