# Razor Proxy [![Supported Versions](https://img.shields.io/pypi/pyversions/razor-proxy.svg)](https://pypi.org/project/razor-proxy)

`Razory Proxy` High Performance Proxy Server (Open Source)<br/>

## Features:
- Easy for used `run proxy server with one command and one click`
- Read requests directly without needing an intermediary like GinCore
- Support authorization proxy (username and password)
- Support All HTTP versions (HTTP1/1 - HTTP/2 - HTTP/3)
- Support All os systems (windows - linux - mac - ios - android...)
- Support All types of networks (Home Networks - Data Center - Server Network - Local Network)
- Support All types of farwards servers (Port forwarding - Nginx server - Apache server)

## How To Use:
- Step 1: You need to install python (any version)

- Step 2: Install razor-proxy
`pip install razor-proxy`

- Step 3: Run razor-proxy
without authorization (recommended to use authorization)

```bash
razor http://host:port
```

with authorization

```bash
razor http://username:password@host:port
```

## How To Make a Computer as public proxy server
- Step 1: Make sure updated the firewall and all system updates

- Step 2: Create port forwarding - nginx server
Example port forwarding : https://www.youtube.com/watch?v=2tIUts0fyFk
Example nginx server: https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/

- Setp 3: Run razor-proxy with the same proxy in the `port forwarding` or `nginx server`