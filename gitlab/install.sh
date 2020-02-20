#!/bin/bash

yum install epel-release -y
yum install ansible -y

python gitlab.py
