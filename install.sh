#!/usr/bin/env bash

apt install speedtest python3-venv -y

python3 -m venv /srv/isp-monitor/venv
/srv/isp-monitor/venv/bin/python3 -m pip install pip setuptools wheel --upgrade --no-cache-dir
/srv/isp-monitor/venv/bin/python3 -m pip install -r /srv/isp-monitor/requirements.txt --upgrade --no-cache-dir

cp /srv/isp-monitor/speedtest.service /etc/systemd/system/
cp /srv/isp-monitor/speedtest.timer /etc/systemd/system/

cp /srv/isp-monitor/visualize.service /etc/systemd/system/
cp /srv/isp-monitor/visualize.timer /etc/systemd/system/

mkdir /srv/isp-monitor/plots -p

systemctl daemon-reload
systemctl enable --now speedtest.timer
systemctl enable --now visualize.timer
