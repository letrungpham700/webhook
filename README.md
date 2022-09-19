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
route:
  receiver: line-noti
receivers:
- name: line-noti
  webhook_configs:
  - url: http://x.x.x.x:5000/
    send_resolved: true
    http_config:
      bearer_token: <my_token>
```
