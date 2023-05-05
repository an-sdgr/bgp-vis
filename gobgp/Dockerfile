# FROM osrg/gobgp:latest
FROM python:3.10.5-alpine3.16

# needed for envsubst
RUN apk add gettext

# not necessary, but nice to have
RUN apk add bash

# again, not necessary, but nice to have
RUN apk add vim

RUN mkdir /root/gobgp
WORKDIR /root/gobgp

# gobgp install
RUN wget https://github.com/osrg/gobgp/releases/download/v3.4.0/gobgp_3.4.0_linux_amd64.tar.gz
RUN tar -xzvf gobgp_3.4.0_linux_amd64.tar.gz
RUN chmod +x gobgp
RUN chmod +x gobgpd

# gobgp config
COPY ./gobgpd-client.conf gobgpd-client.template
COPY ./gobgpd-rr.conf gobgpd-rr.template

# entrypoint
COPY ./entrypoint.sh /root/gobgp/entrypoint.sh
RUN chmod +x /root/gobgp/entrypoint.sh
ENTRYPOINT /root/gobgp/entrypoint.sh
