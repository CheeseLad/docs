# CSC1047 Practical
    
    

## Description

CSC1047 Practical: Which AI API is better at coding?: Ancient Brain & Javascript: Grade 100%

## Docker Compose File

```yaml
services:
  csc1047-practical:
    image: ghcr.io/cheeselad/csc1047-practical:latest
    container_name: csc1047-practical
    restart: unless-stopped
    ports:
      - "3018:80"
```

## Notes

- Access `csc1047-practical` at [https://csc1047-practical.jakefarrell.ie](https://csc1047-practical.jakefarrell.ie) (Publicly Accessible)