import json
import os

class kegman_conf():
  def __init__(self, CP=None):
    self.conf = self.read_config()
    if CP is not None:
      self.init_config(CP)

  def init_config(self, CP):
    write_conf = False
    if self.conf['tuneGernby'] != "1":
      self.conf['tuneGernby'] = str(1)
      write_conf = True
	
    # only fetch Kp, Ki, Kf sR and sRC from interface.py if it's a PID controlled car
    if CP.lateralTuning.which() == 'pid':
      if self.conf['Kp'] == "-1":
        self.conf['Kp'] = str(round(CP.lateralTuning.pid.kpV[0],3))
        write_conf = True
      if self.conf['Ki'] == "-1":
        self.conf['Ki'] = str(round(CP.lateralTuning.pid.kiV[0],3))
        write_conf = True
      if self.conf['Kf'] == "-1":
        self.conf['Kf'] = str('{:f}'.format(CP.lateralTuning.pid.kf))
        write_conf = True
    elif CP.lateralTuning.which() == 'indi':
      if self.conf['outerLG'] == "-1":
        self.conf['outerLG'] = str(round(CP.lateralTuning.indi.outerLoopGain,2))
        write_conf = True
      if self.conf['innerLG'] == "-1":
        self.conf['innerLG'] = str(round(CP.lateralTuning.indi.innerLoopGain,2))
        write_conf = True
      if self.conf['timeConst'] == "-1":
        self.conf['timeConst'] = str(round(CP.lateralTuning.indi.timeConstant,2))
        write_conf = True
      if self.conf['actEffect'] == "-1":
        self.conf['actEffect'] = str(round(CP.lateralTuning.indi.actuatorEffectiveness,2))
        write_conf = True
    elif CP.lateralTuning.which() == 'lqr':
      if self.conf['scale'] == "-1":
        self.conf['scale'] = str(round(CP.lateralTuning.lqr.scale,2))
        write_conf = True
      if self.conf['ki'] == "-1":
        self.conf['ki'] = str(round(CP.lateralTuning.lqr.ki,3))
        write_conf = True
      if self.conf['dc_gain'] == "-1":
        self.conf['dc_gain'] = str('{:f}'.format(CP.lateralTuning.lqr.dcGain))
        write_conf = True
    
    if self.conf['steerRatio'] == "-1":
      self.conf['steerRatio'] = str(round(CP.steerRatio,3))
      write_conf = True
    
    if self.conf['steerRateCost'] == "-1":
      self.conf['steerRateCost'] = str(round(CP.steerRateCost,3))
      write_conf = True

    if write_conf:
      self.write_config(self.config)

  def read_config(self):
    self.element_updated = False

    if os.path.isfile('/data/kegman.json'):
      with open('/data/kegman.json', 'r') as f:
        self.config = json.load(f)

      if "cameraOffset" not in self.config:
        self.config.update({"cameraOffset":"0.06"})
        self.element_updated = True

      if "battPercOff" not in self.config:
        self.config.update({"battPercOff":"100"})
        self.config.update({"carVoltageMinEonShutdown":"11800"})
        self.element_updated = True

      if "tuneGernby" not in self.config:
        self.config.update({"tuneGernby":"1"})
        self.config.update({"Kp":"-1"})
        self.config.update({"Ki":"-1"})
        self.element_updated = True

      if "liveParams" not in self.config:
        self.config.update({"liveParams":"1"})
        self.element_updated = True
	
      if "steerRatio" not in self.config:
        self.config.update({"steerRatio":"-1"})
        self.config.update({"steerRateCost":"-1"})
        self.element_updated = True
	
      if "deadzone" not in self.config:
        self.config.update({"deadzone":"0.1"})
        self.element_updated = True
	
      if "Kf" not in self.config:
        self.config.update({"Kf":"-1"})
        self.element_updated = True
	
      if "sR_boost" not in self.config:
        self.config.update({"sR_boost":"0"})
        self.config.update({"sR_BP0":"0"})
        self.config.update({"sR_BP1":"0"})
        self.config.update({"sR_time":"0.2"})
        self.element_updated = True

      if "ALCnudgeLess" not in self.config:
        self.config.update({"ALCnudgeLess":"1"})
        self.config.update({"ALCminSpeed":"60"})
        self.element_updated = True

      if "ALCtimer" not in self.config:
        self.config.update({"ALCtimer":"1.0"})
        self.element_updated = True

      if "getOffAlert" not in self.config:
        self.config.update({"getOffAlert":"1"})
        self.config.update({"deviceOffTimer":"30"})
        self.element_updated = True

      if "outerLG" not in self.config:
        self.config.update({"outerLG":"-1"})
        self.config.update({"innerLG":"-1"})
        self.config.update({"timeConst":"-1"})
        self.config.update({"actEffect":"-1"})
        self.element_updated = True

      if "scale" not in self.config:
        self.config.update({"scale":"-1"})
        self.config.update({"ki":"-1"})
        self.config.update({"dc_gain":"-1"})
        self.element_updated = True


      if self.element_updated:
        print("updated")
        self.write_config(self.config)

    else:
      self.config = {"cameraOffset":"0.06", "battChargeMin":"70", "battChargeMax":"80", \
                     "wheelTouchSeconds":"30000", "battPercOff":"100", "carVoltageMinEonShutdown":"11800", \
                     "tuneGernby":"1", "getOffAlert":"1", "deviceOffTimer":"30", \
                     "Kp":"-1", "Ki":"-1", "Kf":"-1", \
                     "outerLG":"-1", "innerLG":"-1", "timeConst":"-1", "actEffect":"-1", \
                     "scale":"-1", "ki":"-1", "dc_gain":"-1", \
                     "steerRatio":"-1", "steerRateCost":"-1", "liveParams":"1", "deadzone":"0.1", \
                     "sR_boost":"0", "sR_BP0":"0", "sR_BP1":"0", "sR_time":"0.2", \
                     "ALCnudgeLess":"1", "ALCminSpeed":"60", "ALCtimer":"1.0"}


      self.write_config(self.config)
    return self.config

  def write_config(self, config):
    try:
      with open('/data/kegman.json', 'w') as f:
        json.dump(self.config, f, indent=2, sort_keys=True)
        os.chmod("/data/kegman.json", 0o764)
    except IOError:
      os.mkdir('/data')
      with open('/data/kegman.json', 'w') as f:
        json.dump(self.config, f, indent=2, sort_keys=True)
        os.chmod("/data/kegman.json", 0o764)
