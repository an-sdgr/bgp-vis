#!/bin/sh

# get system IP address, export for envsubst
IP=$(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1)
export IP

# render the template using environment vars
# the $CONF variable determines which template is chosen, the rr or the client
envsubst < "/gobgp/$CONF.template" > /gobgp/gobgpd.conf

# debug info, looks nice
echo "starting $CONF id $IP AS $AS"

# run gobgp with our config file
exec /gobgp/gobgpd -f /gobgp/gobgpd.conf
