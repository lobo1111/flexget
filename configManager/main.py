import structure
import sys
import yaml

user = sys.argv[1]
list = sys.argv[2]
timeframe = sys.argv[3]
quality = sys.argv[4]
structure.config['templates']['tv']['configure_series']['settings']['quality'] = quality
structure.config['templates']['tv']['configure_series']['settings']['timeframe'] = timeframe
structure.config['templates']['tv']['configure_series']['from']['trakt_list']['username'] = user
structure.config['templates']['tv']['configure_series']['from']['trakt_list']['list'] = list
with open(structure.path, 'w') as outfile:
    outfile.write(yaml.dump(structure.config, default_flow_style=True))
