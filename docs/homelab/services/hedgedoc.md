# Hedgedoc
    
    

## Description

Hedgedoc is a self-hosted note-taking and collaborative writing platform that allows users to create and edit documents in real-time. Its purpose is to provide a simple and secure way for individuals or teams to work together on notes, documents, and ideas. Hedgedoc features a distraction-free editor, support for markdown formatting, and real-time collaboration, making it a great tool for homelab users. With Hedgedoc, users can host their own instance, keeping control over their data and privacy.

## Docker Compose File

```yaml
services:
  hedgedoc-database:
    image: postgres:13.4-alpine
    hostname: hedgedoc-database
    container_name: hedgedoc-database
    environment:
      - POSTGRES_USER=hedgedoc
      - POSTGRES_PASSWORD=$POSTGRES_PASSWORD
      - POSTGRES_DB=hedgedoc
    volumes:
      - database:/var/lib/postgresql/data
    restart: unless-stopped
  hedgedoc:
    image: quay.io/hedgedoc/hedgedoc:latest
    hostname: hedgedoc
    container_name: hedgedoc
    environment:
      - CMD_DB_URL=$CMD_DB_URL
      - CMD_DOMAIN=md.jakefarrell.ie
      - CMD_IMAGE_UPLOAD_TYPE=filesystem
      - CMD_IMAGE_UPLOAD_PATH=/hedgedoc/public/uploads
      - CMD_EMAIL=true
      - CMD_ALLOW_EMAIL_REGISTER=true
      - CMD_PROTOCOL_USESSL=true
      - CMD_SESSION_SECRET=$CMD_SESSION_SECRET

    volumes:
      - ~/storage/hedgedoc/uploads:/hedgedoc/public/uploads
    ports:
      - "3000:3000"
    restart: unless-stopped
    depends_on:
      - hedgedoc-database
volumes:
  database:
  uploads:
```

## Notes

- Access `hedgedoc` at [https://md.jakefarrell.ie](https://md.jakefarrell.ie) (Publicly Accessible)