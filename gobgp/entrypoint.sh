#!/bin/sh

# handle SIGINT and SIGTERM properly
trap "exit" INT
trap "exit" TERM

# get system IP address, export for envsubst
IP=$(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1)
export IP

# render the template using environment vars
# the $CONF variable determines which template is chosen, the rr or the client
envsubst < "/gobgp/templates/$CONF.yaml" > /gobgp/gobgpd.yaml

# debug info, looks nice
echo "starting $CONF id $IP AS $AS"

/gobgp/gobgp global rib add 10.0.0.0/24 -a ipv4

# run gobgp with our config file
exec /gobgp/gobgpd -t yaml -f /gobgp/gobgpd.yaml
