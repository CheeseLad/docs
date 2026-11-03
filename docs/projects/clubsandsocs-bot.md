# clubsandsocs-bot

*[GitHub Repository Link](https://github.com/CheeseLad/clubsandsocs-bot)*

A Discord bot for getting events, committee members, and more from Clubs and Societies websites.

## Invite the bot to your server

[Click here to invite the bot to your server](https://discord.com/oauth2/authorize?client_id=1284649108711276555&permissions=8&integration_type=0&scope=bot)

## Docker Deployment

### Prerequisites
- Docker and Docker Compose installed
- Environment variables configured

### Quick Start with Docker Compose

1. Clone this repository
2. Copy `.env.example` to `.env` and fill in your environment variables:
   ```bash
   cp .env.example .env
   ```

3. Edit `.env` with your actual values:
   ```env
   DISCORD_TOKEN=your_discord_bot_token_here
   DISCORD_CLIENT_ID=your_discord_client_id_here
   DISCORD_GUILD_ID=your_discord_guild_id_here
   CLUBS_AND_SOCS_WEBSITE=your_clubs_and_socs_website_endpoint_here
   ```

4. Run with Docker Compose:
   ```bash
   docker-compose up -d
   ```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DISCORD_TOKEN` | Your Discord bot token | Yes |
| `DISCORD_CLIENT_ID` | Your Discord application client ID | Yes |
| `DISCORD_GUILD_ID` | Your Discord guild (server) ID for guild commands | No |
| `CLUBS_AND_SOCS_WEBSITE` | Base endpoint for clubs and societies API | Yes |

### Docker Image

The Docker image is automatically built and published to GitHub Container Registry on every push to the main branch. You can pull it directly:

```bash
docker pull ghcr.io/cheeselad/clubsandsocs-bot:latest
```
