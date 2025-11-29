# The Experiment
    
    

## Description

The Experiment is a bot like no other. It features a curated collection of GIFs from discord users all across the globe and is self-moderated by user input!

## Docker Compose File

```yaml
services:
  the-experiment:
    container_name: the-experiment
    restart: unless-stopped
    build: ~/storage/the-experiment
    volumes:
      - ~/storage/the-experiment/app:/app

```

## Notes

None