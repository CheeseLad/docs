# DCUMPS Website
    
    

## Description

*Full Stack Website Built For DCU Media Production Society*

Tech Stack Used:
- Django
- Python
- Bootstrap
- JavaScript
- SQLite
- Docker
- [Clubs & Socs API](https://github.com/CheeseLad/clubsandsocs-api)
- WordPress REST API

Website Content & Features:
- Society information, contact details & social media accounts list
- Preview of latest articles from [thecollegeview.ie](https://thecollegeview.ie) using the WordPress REST API
- Blog system containing 2018-2021 blogs imported from Squarespace with sharing options
- Automated event information from my custom [Clubs & Socs API](https://github.com/CheeseLad/clubsandsocs-api) 
- Automated querying of YouTube videos
- Twitch stream with automated radio show timetable
- Sponsor list & testimonials
- Meet the committee page with committee video, committee history and contact information

## Docker Compose File

```yaml
services:
  dcumps-website:
    image: ghcr.io/cheeselad/dcumps-website-django:latest
    container_name: dcumps-website
    restart: unless-stopped
    ports:
      - "3020:8000"
    environment:
      # Django Settings
      - DEBUG=${DEBUG}
      - SECRET_KEY=${SECRET_KEY}
      - ALLOWED_HOSTS=${ALLOWED_HOSTS}
      - ADMIN_ENABLED=${ADMIN_ENABLED}
      
      # External Data Configuration
      - YOUTUBE_CHANNEL_ID=${YOUTUBE_CHANNEL_ID}
      - CLUBS_SOCS_API_URL=${CLUBS_SOCS_API_URL}
      - THECOLLEGEVIEW_BASE_URL=${THECOLLEGEVIEW_BASE_URL}
      
      # Google Sheets IDs
      - LINKTREE_MAIN_SHEET_ID=${LINKTREE_MAIN_SHEET_ID}
      - LINKTREE_TV_SHEET_ID=${LINKTREE_TV_SHEET_ID}
      - LINKTREE_FM_SHEET_ID=${LINKTREE_FM_SHEET_ID}
      - LINKTREE_TCV_SHEET_ID=${LINKTREE_TCV_SHEET_ID}
      - LINKTREE_DEV_SHEET_ID=${LINKTREE_DEV_SHEET_ID}

      # WordPress API Configuration
      - WP_API_USERNAME=${WP_API_USERNAME}
      - WP_API_PASSWORD=${WP_API_PASSWORD}
    networks:
      - cheeselab

networks:
  cheeselab:
    external: true
```

## Notes

- Access `dcumps-website` at [https://dcumps.jakefarrell.ie](https://dcumps.jakefarrell.ie) (Publicly Accessible)