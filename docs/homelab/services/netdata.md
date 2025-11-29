# Netdata
    
    

## Description

Netdata is a real-time monitoring and troubleshooting tool for your homelab or home server. Its purpose is to provide detailed insights into system performance, metrics, and logs, helping you identify issues before they become major problems. With features like customizable dashboards, alerts, and a wide range of supported platforms, Netdata is a powerful tool for keeping your homelab running smoothly. It's also highly extensible, with a large community of users contributing plugins and other integrations to help you get the most out of the service.

## Docker Compose File

```yaml
services:
  netdata:
    image: netdata/netdata
    container_name: netdata
    pid: host
    network_mode: host
    restart: unless-stopped
    cap_add:
      - SYS_PTRACE
      - SYS_ADMIN
    security_opt:
      - apparmor:unconfined
    volumes:
      - netdataconfig:/etc/netdata
      - netdatalib:/var/lib/netdata
      - netdatacache:/var/cache/netdata
      - /:/host/root:ro,rslave
      - /etc/passwd:/host/etc/passwd:ro
      - /etc/group:/host/etc/group:ro
      - /etc/localtime:/etc/localtime:ro
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /etc/os-release:/host/etc/os-release:ro
      - /var/log:/host/var/log:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - /run/dbus:/run/dbus:ro

volumes:
  netdataconfig:
  netdatalib:
  netdatacache:
```

## Notes

None