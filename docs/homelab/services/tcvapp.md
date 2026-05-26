# The College View App
    
    

## Description

Developing an iOS & Android app for The College View - DCU's independent student newspaper using Flutter and the WordPress REST API. The app allows users to view articles and categories, submit their own articles and search for articles, the app is planned to be released on both the Apple App Store and the Google Play Store.

Technologies Used:
- Flutter
- WordPress REST API
- Dart

## Docker Compose File

```yaml
services:
  tcvapp:
    image: nginx:latest
    container_name: tcvapp
    restart: unless-stopped
    volumes:
      - ~/storage/tcvapp:/usr/share/nginx/html
    ports:
      - "3023:80"
    networks:
      - cheeselab

networks:
  cheeselab:
    external: true
```

## Notes

- Access `tcvapp` at [https://tcvapp.jakefarrell.ie](https://tcvapp.jakefarrell.ie) (Publicly Accessible)