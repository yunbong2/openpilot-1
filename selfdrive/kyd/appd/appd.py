#!/usr/bin/env python3.7
import time
import subprocess
import cereal
import cereal.messaging as messaging
ThermalStatus = cereal.log.ThermalData.ThermalStatus
from selfdrive.swaglog import cloudlog
from common.realtime import sec_since_boot
from common.params import Params, put_nonblocking
params = Params()
from math import floor
import re
import os

class App():

  # app type
  TYPE_GPS = 0
  TYPE_SERVICE = 1
  TYPE_GPS_SERVICE = 2
  TYPE_FULLSCREEN = 3
  TYPE_UTIL = 4

  # manual switch stats
  MANUAL_OFF = "-1"
  MANUAL_IDLE = "0"
  MANUAL_ON = "1"

  def appops_set(self, package, op, mode):
    self.system(f"LD_LIBRARY_PATH= appops set {package} {op} {mode}")

  def pm_grant(self, package, permission):
    self.system(f"pm grant {package} {permission}")

  def set_package_permissions(self):
    if self.permissions is not None:
      for permission in self.permissions:
        self.pm_grant(self.app, permission)
    if self.opts is not None:
      for opt in self.opts:
        self.appops_set(self.app, opt, "allow")

  def __init__(self, app, activity, enable_param, auto_run_param, manual_ctrl_param, app_type, permissions, opts):
    self.app = app
    # main activity
    self.activity = activity
    # read enable param
    self.enable_param = enable_param
    # read auto run param
    self.auto_run_param = auto_run_param
    # read manual run param
    self.manual_ctrl_param = manual_ctrl_param
    # if it's a service app, we do not kill if device is too hot
    self.app_type = app_type
    # app permissions
    self.permissions = permissions
    # app options
    self.opts = opts

    self.is_installed = False
    self.last_is_enabled = False
    self.is_auto_runnable = False
    self.is_running = False
    self.manual_ctrl_status = self.MANUAL_IDLE
    self.manually_ctrled = False


  def run(self, force = False):
      # app is manually ctrl, we record that
    if self.manual_ctrl_param is not None and self.manual_ctrl_status == self.MANUAL_ON:
       put_nonblocking(self.manual_ctrl_param, '0')
       self.manually_ctrled = True
       self.is_running = False

      # only run app if it's not running
       self.system("am start -n %s/%s" % (self.app, self.activity))
    self.is_running = True

  def kill(self, force = False):
      # app is manually ctrl, we record that
    if self.manual_ctrl_param is not None and self.manual_ctrl_status == self.MANUAL_OFF:
      put_nonblocking(self.manual_ctrl_param, '0')
      self.manually_ctrled = True
      self.is_running = True

      # only kill app if it's running
    if force or self.is_running:
      if self.app_type == self.TYPE_GPS_SERVICE:
        self.appops_set(self.app, "android:mock_location", "deny")
        self.system("pkill %s" % self.app)
        self.is_running = False

  def system(self, cmd):
    try:
      subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
      cloudlog.event("running failed",
                     cmd=e.cmd,
                     output=e.output[-1024:],
                     returncode=e.returncode)

def init_apps(apps):
  apps.append(App(
    "com.mixplorer",
    "com.mixplorer.activities.BrowseActivity",
    [],
    None,
    "OpkrRunMixplorer",
    App.TYPE_UTIL,
    [
      "android.permission.READ_EXTERNAL_STORAGE",
      "android.permission.WRITE_EXTERNAL_STORAGE",
    ],
    [],
  ))
  apps.append(App(
    "com.quickedit",
    "com.quickedit.activities.BrowseActivity",
    [],
    None,
    "OpkrRunQuickedit",
    App.TYPE_UTIL,
    [
      "android.permission.READ_EXTERNAL_STORAGE",
      "android.permission.WRITE_EXTERNAL_STORAGE",
    ],
    [],
  ))

def main():
  apps = []

  last_started = False
  thermal_sock = messaging.sub_sock('thermal')

  frame = 0
  start_delay = None
  stop_delay = None
  allow_auto_run = True
  last_thermal_status = None
  thermal_status = None
  start_ts = sec_since_boot()
  init_done = False

  while 1: #has_enabled_apps:
    if not init_done:
      if sec_since_boot() - start_ts >= 10:
        init_apps(apps)
        init_done = True

if __name__ == "__main__":
  main()
  