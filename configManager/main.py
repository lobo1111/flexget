import structure
import save
import os.path
import sys

if not os.path.isfile(structure.path):
    user = sys.argv[1]
    list = sys.argv[2]
    timeframe = sys.argv[3]
    quality = sys.argv[4]
    with open(structure.path, 'rw') as ymlfile:
        cfg = yaml.load(ymlfile)
        cfg['templates']['tv']['configure_series']['settings']['default']['quality'] = quality
        cfg['templates']['tv']['configure_series']['settings']['default']['timeframe'] = timeframe
        cfg['templates']['tv']['configure_series']['settings']['default']['from']['trakt_list']['username'] = user
        cfg['templates']['tv']['configure_series']['settings']['default']['from']['trakt_list']['list'] = list
        save.saveConfig(cfg)
