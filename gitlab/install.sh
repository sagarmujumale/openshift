#!/bin/bash

yum install epel-release -y
yum install ansible docker -y
systemctl restart docker

python gitlab.py
