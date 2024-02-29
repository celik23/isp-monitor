#!/usr/bin/env bash

sudo systemctl stop speedtest.timer
sudo systemctl stop speedtest.service
sudo systemctl disable speedtest.timer
sudo systemctl disable speedtest.service

sudo rm /etc/systemd/system/speedtest.timer
sudo rm /etc/systemd/system/speedtest.service

sudo systemctl daemon-reload
