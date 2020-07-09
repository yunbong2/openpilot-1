#!/usr/bin/bash

mount -o remount,rw /system
cp -f /data/openpilot/selfdrive/ui/* /system/comma/openpilot/selfdrive/ui/
mount -o remount,r /system