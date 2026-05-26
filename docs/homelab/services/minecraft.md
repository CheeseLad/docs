# Minecraft
    
    

## Description

Minecraft is a popular online multiplayer game that can be self-hosted on a home server, allowing you to create your own private server for friends and family. The itzg/minecraft-server:latest image provides a simple way to set up and manage a Minecraft server, automating tasks like backups and updates. This service lets you customize your server with various plugins and mods, giving you control over the gameplay experience. By hosting your own Minecraft server, you can ensure a lag-free and secure environment for players to build and explore together.

## Docker Compose File

```yaml
services:
  minecraft:
    image: itzg/minecraft-server:latest
    container_name: minecraft
    restart: unless-stopped
    pull_policy: daily
    tty: true
    stdin_open: true
    ports:
      - "25565:25565"
    environment:
      EULA: "TRUE"
    volumes:
      # attach the relative directory 'data' to the container's /data path
      - ~/storage/minecraft:/data
```

## Notes

- Access `minecraft` at [http://cheeselab:25565](http://cheeselab:25565) (Local Network Only)