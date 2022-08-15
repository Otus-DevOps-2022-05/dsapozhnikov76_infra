#!/bin/bash

apt update
sleep 10
apt install -y mongodb
systemctl start mongodb
systemctl enable mongodb
