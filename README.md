# Line Notification Gateway #

Line Notification Gateway for Alertmanager (Promtheus).

## Installation ##

```bash
git clone https://github.com/letrungpham700/webhook.git
cd webhook

```

## Usage ##

Set receiver of generic webhook from Alertmanager.

```yaml
global:
  resolve_timeout: 5m
route:
  receiver: line-noti
  group_by: ['job','instance','severity','alertname']
  group_interval: 10s
  repeat_interval: 1m
receivers:
- name: line-noti
  webhook_configs:
  - url: 'http://x.x.x.x:5000/webhook'
    send_resolved: true
    http_config:
      bearer_token: <mytoken>
```
