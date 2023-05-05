FROM alpine:3.17

ENV GOBGP_VERSION=3.14.0

RUN apk add --no-cache gettext bash && \
    rm -fr /var/cache/apk/*

RUN mkdir /gobgp
WORKDIR /gobgp

# gobgp install
RUN wget https://github.com/osrg/gobgp/releases/download/v${GOBGP_VERSION}/gobgp_${GOBGP_VERSION}_linux_amd64.tar.gz
RUN tar -xzvf gobgp_${GOBGP_VERSION}_linux_amd64.tar.gz
RUN rm gobgp_${GOBGP_VERSION}_linux_amd64.tar.gz
RUN chmod +x gobgp
RUN chmod +x gobgpd

# add gobgp to path
RUN echo "PATH=$PATH:/gobgp" > /root/.bashrc

# gobgp config
RUN mkdir templates
COPY ./gobgpd-client.conf templates/gobgpd-client.template
COPY ./gobgpd-rr.conf templates/gobgpd-rr.template

# entrypoint
COPY ./entrypoint.sh /gobgp/entrypoint.sh
RUN chmod +x /gobgp/entrypoint.sh
#ENTRYPOINT [ "/gobgp/entrypoint.sh" ]

# tini, needed if you omit init: true in compose
#RUN apk add tini
#ENTRYPOINT ["tini", "--"]

# Run your program under Tini
CMD ["/gobgp/entrypoint.sh"]
