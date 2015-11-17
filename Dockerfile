FROM python:2.7

RUN pip install -I flexget

VOLUME /opt/flexget
VOLUME /opt/torrents

COPY scripts/* /usr/bin/
RUN chmod +x /usr/bin/*

COPY setup.sh /opt/
COPY start.sh /opt/
RUN chmod +x /opt/setup.sh
RUN chmod +x /opt/start.sh

COPY configManager opt/configManager/

WORKDIR /opt/
