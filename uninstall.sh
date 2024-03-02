#!/usr/bin/env bash

systemctl stop speedtest.timer
systemctl stop speedtest.service
systemctl disable speedtest.timer
systemctl disable speedtest.service

rm /etc/systemd/system/speedtest.timer
rm /etc/systemd/system/speedtest.service

systemctl stop visualize.timer
systemctl stop visualize.service
systemctl disable visualize.timer
systemctl disable visualize.service

rm /etc/systemd/system/visualize.timer
rm /etc/systemd/system/visualize.service

systemctl daemon-reload
