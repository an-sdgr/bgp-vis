#!/bin/sh

# get system IP address, export for envsubst
IP=$(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1)
export IP

# render the template using environment vars
envsubst < "/root/gobgp/$CONF.template" > /root/gobgp/gobgpd.conf

echo "starting $CONF id $IP AS $AS"

# run gobgp with our config file
exec /root/gobgp/gobgpd -f /root/gobgp/gobgpd.conf
