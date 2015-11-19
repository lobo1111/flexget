import structure
import save
import os.path
import sys

user = sys.argv[1]
list = sys.argv[2]
timeframe = sys.argv[3]
quality = sys.argv[4]
structure.default['templates']['tv']['configure_series']['settings']['default']['quality'] = quality
structure.default['templates']['tv']['configure_series']['settings']['default']['timeframe'] = timeframe
structure.default['templates']['tv']['configure_series']['settings']['default']['from']['trakt_list']['username'] = user
structure.default['templates']['tv']['configure_series']['settings']['default']['from']['trakt_list']['list'] = list
save.saveConfig(structure.default)
