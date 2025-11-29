# Clubs & Socs API
    
    

## Description

Allows you to get information about societies and clubs from university websites using the [Assure Memberships Platform](https://assurememberships.com) for use in other applications.

## Supported Sites

- [DCU Clubs & Socs](https://dcuclubsandsocs.ie)
  - Site Code: `dcuclubsandsocs.ie`
- [MU Clubs & Societies](https://mulife.ie/)
  - Site Code: `mulife.ie`
- [SETU Waterford Sports Clubs & Societies](https://waterford.sportsclubsandsocieties.setu.ie/)
  - Site Code: `waterford.sportsclubsandsocieties.setu.ie`
- [UL Clubs & Societies](https://ulwolves.ie/)
  - Site Code: `ulwolves.ie`
- [ATU Sligo Clubs & Socs](https://sligo.atusulife.ie/)
  - Site Code: `sligo.atusulife.ie`
- [ATU Donegal Clubs & Socs](https://donegal.atusulife.ie/)
  - Site Code: `donegal.atusulife.ie`
  
## Supported Types

- `society`
- `club`

## Installation

1. Clone the repository
2. Run `pip install -r requirements.txt` to install the required packages
3. Run `flask run` to start the API server

## Usage

The API has the following endpoints:

- `/<site>/<type>/<society>/events` - Get all upcoming events for a society/club
- `/<site>/<type>/<society>/committee` - Get the committee information for a society/club
- `/<site>/<type>/<society>/gallery` - Get the gallery photos for a society/club
- `/<site>/<type>/<society>/activities` - Get all weekly activities for a society/club

## API Usage Examples

- `/dcuclubsandsocs.ie/society/redbrick/events` - Get all upcoming events for Redbrick Society in DCU
- `/mulife.ie/society/esn/committee` - Get the committee information for the Erasmus Student Network Society in Maynooth University
- `/dcuclubsandsocs.ie/society/media-production/gallery` - Get the gallery photos for the Media Production Society in DCU
- `/mulife.ie/club/table-tennis/activities` - Get all weekly activities for the Table Tennis Club in Maynooth University

## Docker Compose File

```yaml
services:
  clubsandsocs-api:
    image: ghcr.io/cheeselad/clubsandsocs-api:latest
    container_name: clubsandsocs-api
    hostname: clubsandsocs-api
    restart: unless-stopped
    environment:
      - PORT=4000
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.clubsandsocs-api.entrypoints=https"
      - "traefik.http.routers.clubsandsocs-api.rule=Host(`clubsandsocs.jakefarrell.ie`)"
      - "traefik.http.services.clubsandsocs-api.loadbalancer.server.port=4000"
      - "traefik.http.routers.clubsandsocs-api.service=clubsandsocs-api"


networks:
  default:
    name: traefik_net
    external: true
```

## Notes

- Access `clubsandsocs-api` at [https://clubsandsocs.jakefarrell.ie](https://clubsandsocs.jakefarrell.ie) (Publicly Accessible via Traefik)