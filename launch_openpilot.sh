#!/usr/bin/bash

if [ ! -f /data/ota_updates ]; then
    /usr/bin/touch /data/ota_updates
fi
/usr/bin/sh /data/openpilot/kyd/fonts/installer.sh &
export PASSIVE="0"
exec ./launch_chffrplus.sh

