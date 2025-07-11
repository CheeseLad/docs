# Pterodactyl
    
    

## Description

Pterodactyl is a free, open-source game server management panel that allows you to easily manage and deploy game servers, like Minecraft or Team Fortress, on your homelab. Its main purpose is to simplify server management, making it easy to create, configure, and monitor game servers. Pterodactyl provides useful features such as automatic updates, backups, and a user-friendly interface to help you manage your game servers. It's a popular choice among gamers and server admins due to its flexibility and customization options.

## Docker Compose File

```yaml
services:
  # Wings is the service that hooks into docker and actually creates your game
  # servers,
  wings:
    image: ghcr.io/pterodactyl/wings:latest
    restart: always
    networks:
      - ptero0
    # These are the ports exposed by Wings, I don't recommend changing them.
    ports:
      - "8443:443"
      - "2022:2022"
    tty: true
    environment:
      TZ: "Europe/Dublin"
      # For ease of setup, this is going to use root user.
      WINGS_UID: 0
      WINGS_GID: 0
      WINGS_USERNAME: root
    # This is where docker will bind certain parts of container to your actual
    # host OS. These locations will be used later.
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock" # DO NOT CHANGE
      - "/var/lib/docker/containers:/var/lib/docker/containers" # DO NOT CHANGE
      - "~/storage/pterodactyl/wings/config:/etc/pterodactyl" # Feel free to change.
      - "/var/lib/pterodactyl:/var/lib/pterodactyl" # DO NOT CHANGE
      - "/var/log/pterodactyl:/var/log/pterodactyl" # DO NOT CHANGE
      - "/tmp/pterodactyl/:/tmp/pterodactyl/" # Recommended not to change.
  # It's a database. Not much else to explain.
  database:
    image: mariadb:10.5
    restart: always
    command: --default-authentication-plugin=mysql_native_password
    volumes:
      - "/opt/pterodactyl/panel/database:/var/lib/mysql"
    environment:
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: "panel"
      MYSQL_USER: "pterodactyl"
  # It's a CACHE database. Not much else to explain.
  cache:
    image: redis:alpine
    restart: always
  # Now the fun part. Your actual panel.
  panel:
    image: ghcr.io/pterodactyl/panel:latest
    restart: always
    # For NGINX Reverse Proxy, I will be using these ports for simplicity.
    ports:
      - "802:80"
      - "4432:443"
    # Links these containers together in a docker network.
    links:
      - database
      - cache
    # This is where docker will bind certain parts of container to your actual
    # host OS. These don't really matter that much.
    volumes:
      - "~/storage/pterodactyl/panel/appvar/:/app/var/"
      - "~/storage/pterodactyl/panel/nginx/:/etc/nginx/http.d/"
      - "~/storage/pterodactyl/panel/logs/:/app/storage/logs"
    # Sets the config stuff
    environment:
      DB_PASSWORD: ${MYSQL_PASSWORD}
      APP_ENV: "production"
      APP_ENVIRONMENT_ONLY: "false"
      CACHE_DRIVER: "redis"
      SESSION_DRIVER: "redis"
      QUEUE_DRIVER: "redis"
      REDIS_HOST: "cache"
      DB_HOST: "database"
      DB_PORT: "3306"
      APP_URL: "https://panel.cablenetwork.xyz"
      APP_TIMEZONE: "Europe/Dublin"
      APP_SERVICE_AUTHOR: "jake_farrell@outlook.com"
# This is Wings' Network. We don't need much depth here, all you need to know, is
# that it allows the passthrough of the ports from Wings.
networks:
  ptero0:
    name: ptero0
    driver: bridge
    ipam:
      config:
        - subnet: "192.55.0.0/16"
    driver_opts:
      com.docker.network.bridge.name: ptero0
```

## Notes

- Access `panel` at [https://panel.cablenetwork.xyz](https://panel.cablenetwork.xyz) (Publicly Accessible)