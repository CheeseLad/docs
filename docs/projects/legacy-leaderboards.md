# Legacy Leaderboards

*[GitHub Repository Link](https://github.com/CheeseLad/legacy-leaderboards)*

Legacy Leaderboards is a Django + Django REST Framework backend that adds global leaderboard and achievement tracking functionality back to Minecraft Legacy Console Edition.

Features include:
- Player profile creation and lookup by UID
- Achievement catalog import and per-player unlock status
- API endpoints to unlock/reset achievements for players
- A server-rendered achievements UI page
- Login/account linking so a website account can be tied to a player UID
- It also stores achievements and each player's unlock status.
- Additional leaderboard endpoints exist in code but are currently commented out in URL routing. (To be implemented in the future)

Check it out here: [legacyleaderboards.jakefarrell.ie](https://legacyleaderboards.jakefarrell.ie/)

# Installation Instructions

1. Download Minecraft LCE from my forked repo: https://github.com/CheeseLad/MinecraftConsoles
2. Launch the game and click on "Achievements" in the main menu, this will open the website in your browser and prompt you to create an account and link it to your player UID.
3. Once logged in, you can view your achievements and their unlock status on by clicking on `My Achievements`.
4. To test it's all working, enter a world and open your inventory, this will unlock the "Open Inventory" achievement. Refresh the achievements page to see it update.

## Main Routes

### Auth + UI

- `GET /` -> login page
- `GET /login/` -> login page
- `GET /create-account/` -> create account + link account to player UID
- `GET|POST /logout/`
- `GET /my-achievements/` -> redirects logged-in user to their achievements page
- `GET /ui/achievements?uid=<player_uid>` -> achievement cards UI for a player

### API

- `GET /api/` -> API root with discovered endpoints
- `GET /api/achievement/list` -> list all achievements
- `POST /api/achievement/add` -> set a player's achievement status to `true`
- `POST /api/achievement/remove` -> set a player's achievement status to `false`
- `GET /api/player?uid=<player_uid>` -> player profile, stats, and achievements
- `POST /api/player/add` -> create player (`uid`, `name`)
