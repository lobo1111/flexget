#!/bin/bash

if [ ! -f /opt/flexget/config.yml ]; then
    /opt/setup.sh
fi

while :
do
	flexget -c /opt/flexget/config.yml execute
	sleep 300
done
