# HedgeDoc

## Description

HedgeDoc (formerly known as CodiMD) is an open-source, web-based, self-hosted, collaborative markdown editor.

You can use it to easily collaborate on notes, graphs and even presentations in real-time. All you need to do is to share your note-link to your co-workers and they’re ready to go.

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
      - CMD_DOMAIN=$CMD_DOMAIN
      - CMD_IMAGE_UPLOAD_TYPE=filesystem
      - CMD_IMAGE_UPLOAD_PATH=/hedgedoc/public/uploads
      - CMD_EMAIL=true
      - CMD_ALLOW_EMAIL_REGISTER=true
      - CMD_PROTOCOL_USESSL=true
      - CMD_SESSION_SECRET=$CMD_SESSION_SECRET

    volumes:
      - ./uploads:/hedgedoc/public/uploads
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

- Access HedgeDoc at [https://md.jakefarrell.ie](https://md.jakefarrell.ie)
- Utilises Cloudflare Zero Trust for security and access control, allowing for secure access to HedgeDoc from anywhere.