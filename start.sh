#!/bin/bash

cd /opt/configManager
python main.py "$TRAKT_USER" "$TRAKT_LIST" "$TIMEFRAME" "$QUALITY" "$RSS" "$CLUSTER_NAME" "$INSTANCE_NAME"

while :
do
        flexget -c /opt/flexget/$CLUSTER_NAME/$INSTANCE_NAME.yml execute
        sleep $SLEEP
done


