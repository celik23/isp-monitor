# ISP Monitor

Hourly internet bandwidth and ping updated on a daily basis. Service is Fiber First's Gigabit plan.

![snapshot](/plots/latest.png)

## Install

```shell
sudo apt update
sudo apt upgrade -y
sudo git clone https://github.com/harrelchris/isp-monitor.git /srv/isp-monitor
sudo bash /srv/isp-monitor/install.sh
```

## Status

```shell
systemctl status speedtest.service
systemctl status speedtest.timer
journalctl -u speedtest.service
journalctl -u speedtest.timer
journalctl -u speedtest -f
```

## Uninstall

```shell
sudo bash isp-monitor/uninstall.sh
systemctl list-unit-files | grep speedtest
```
