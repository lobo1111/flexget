import structure
import sys
import yaml

user = sys.argv[1]
list = sys.argv[2]
timeframe = sys.argv[3]
quality = sys.argv[4]
print structure.default
structure.default['templates']['tv']['configure_series']['settings']['default']['quality'] = quality
structure.default['templates']['tv']['configure_series']['settings']['default']['timeframe'] = timeframe
structure.default['templates']['tv']['configure_series']['settings']['default']['from']['trakt_list']['username'] = user
structure.default['templates']['tv']['configure_series']['settings']['default']['from']['trakt_list']['list'] = list
with open(structure.path, 'w') as outfile:
    outfile.write(yaml.dump(structure.default, default_flow_style=True))
