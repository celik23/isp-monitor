# ISP Monitor

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
```

## Uninstall

```shell
sudo bash isp-monitor/uninstall.sh
systemctl list-unit-files | grep speedtest
```
