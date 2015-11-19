#!/bin/bash

cd /opt/configManager
python main.py "$TRAKT_USER" "$TRAKT_LIST" "$TIMEFRAME" "$QUALITY"

while :
do
	flexget -c /opt/flexget/config.yml execute
	sleep $SLEEP
done
