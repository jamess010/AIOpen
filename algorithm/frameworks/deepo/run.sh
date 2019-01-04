#!/bin/bash
/usr/sbin/sshd
jupyter notebook --allow-root
while ((1)); do
    sleep 31536000
done
