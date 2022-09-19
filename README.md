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
receivers:
  - name: 'line'
    webhook_configs:
      - url: 'http://x.x.x.x:5000/webhook'
        http_config:
          bearer_token: '« YOUR_LINE_API_TOKEN »'
```
