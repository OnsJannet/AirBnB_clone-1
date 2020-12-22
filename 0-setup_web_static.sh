#!/usr/bin/env bash
# Configuring a new server

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "testing nginx" >> /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/current /data/web_static/releases/test/
sudo chown ubuntu:ubuntu /data/
sudo echo "location /hbnb_static/ {\nalias /data/web_static/current;\n}" >> /etc/nginx/sites-enabled/default 
service nginx restart
