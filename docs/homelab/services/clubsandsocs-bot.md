# Clubsandsocs Bot
    
    

## Description

A Discord bot for getting events, committee members, and more from Clubs and Societies websites.

## Docker Compose File

```yaml
services:
  clubsandsocs-bot:
    image: ghcr.io/cheeselad/clubsandsocs-bot:latest
    container_name: clubsandsocs-bot
    restart: unless-stopped
    environment:
      - DISCORD_TOKEN=${DISCORD_TOKEN}
      - DISCORD_CLIENT_ID=${DISCORD_CLIENT_ID}
      - DISCORD_GUILD_ID=${DISCORD_GUILD_ID}
      - CLUBS_AND_SOCS_WEBSITE=${CLUBS_AND_SOCS_WEBSITE}

```

## Notes

None