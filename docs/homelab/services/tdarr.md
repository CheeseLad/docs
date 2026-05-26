# Tdarr
    
    

## Description

Tdarr is a service that helps organize and manage your media collection by automatically scanning and identifying your movies and TV shows. Its purpose is to make it easy to maintain a tidy and cataloged library, saving you time and effort in the process. One of its useful features is the ability to detect and fix incorrect file names, metadata, and subtitles, ensuring your media library is accurate and easy to browse. Tdarr integrates well with other homelab services, making it a great addition to any media enthusiast's setup.

## Docker Compose File

```yaml
services:
  tdarr:
    container_name: tdarr
    image: ghcr.io/haveagitgat/tdarr:latest
    restart: unless-stopped
    network_mode: bridge
    ports:
      - 8265:8265 # webUI port
      - 8266:8266 # server port
    environment:
      - TZ=Europe/London
      - PUID=1000
      - PGID=1000
      - UMASK_SET=002
      - serverIP=192.168.1.2
      - serverPort=8266
      - webUIPort=8265
      - internalNode=true
      - inContainer=true
      - ffmpegVersion=7
      - nodeName=CheeseLabInternalNode
      - auth=false
      - openBrowser=true
      - maxLogSizeMB=10
      - cronPluginUpdate=
    volumes:
      - ~/storage/tdarr/server:/app/server
      - ~/storage/tdarr/configs:/app/configs
      - ~/storage/tdarr/logs:/app/logs
      - /media:/media
      - ~/storage/tdarr/transcode_cache:/temp
      - /mnt/storage-hdd/Media/Movies:/movies

    devices:
      - /dev/dri:/dev/dri

    group_add:
      - "105" # render group
      - "44"  # video group
    

# node example
  tdarr-node:
    container_name: tdarr-node
    image: ghcr.io/haveagitgat/tdarr_node:latest
    restart: unless-stopped
    network_mode: service:tdarr
    environment:
      - TZ=Europe/London
      - PUID=1000
      - PGID=1000
      - UMASK_SET=002
      - nodeName=CheeseLabExternalNode
      - serverIP=192.168.1.2
      - serverPort=8266
      - inContainer=true
      - ffmpegVersion=7
      - nodeType=mapped
      - priority=-1
      - cronPluginUpdate=
      - apiKey=
      - maxLogSizeMB=10
      - pollInterval=2000
      - startPaused=false
      - transcodegpuWorkers=0
      - transcodecpuWorkers=1
      - healthcheckgpuWorkers=0
      - healthcheckcpuWorkers=1

    volumes:
      - ~/storage/tdarr/configs:/app/configs
      - ~/storage/tdarr/logs:/app/logs
      - /media:/media
      - ~/storage/tdarr/transcode_cache:/temp
      - /mnt/storage-hdd/Media/Movies:/movies

    devices:
      - /dev/dri:/dev/dri

    group_add:
      - "105" # render group
      - "44"  # video group
```

## Notes

- Access `tdarr` at [http://cheeselab:8265](http://cheeselab:8265) (Local Network Only)