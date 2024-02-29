#!/usr/bin/env bash

apt install speedtest

cp /srv/isp-monitor/speedtest.service /etc/systemd/system/
cp /srv/isp-monitor/speedtest.timer /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now speedtest.timer
