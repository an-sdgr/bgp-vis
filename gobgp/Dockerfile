FROM alpine:3.17

# needed for envsubst
RUN apk add gettext

# not necessary, but nice to have
RUN apk add bash

# again, not necessary, but nice to have
RUN apk add vim

RUN mkdir /gobgp
WORKDIR /gobgp

# gobgp install
RUN wget https://github.com/osrg/gobgp/releases/download/v3.4.0/gobgp_3.4.0_linux_amd64.tar.gz
RUN tar -xzvf gobgp_3.4.0_linux_amd64.tar.gz
RUN chmod +x gobgp
RUN chmod +x gobgpd

# add gobgp to path
RUN echo "PATH=$PATH:/gobgp" > /root/.bashrc

# gobgp config
COPY ./gobgpd-client.conf gobgpd-client.template
COPY ./gobgpd-rr.conf gobgpd-rr.template

# entrypoint
COPY ./entrypoint.sh /gobgp/entrypoint.sh
RUN chmod +x /gobgp/entrypoint.sh
ENTRYPOINT /gobgp/entrypoint.sh
