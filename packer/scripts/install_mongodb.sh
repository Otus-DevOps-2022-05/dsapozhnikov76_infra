#!/bin/bash

apt install -y mongodb
systemctl start mongodb
systemctl enable mongodb
