#!/bin/bash

if [ -f /opt/setup.sh ]
then
    /opt/setup.sh
    rm /opt/setup.sh 
fi

while :
do
	flexget -c /opt/flexget/config.yml execute
	sleep 300
done
