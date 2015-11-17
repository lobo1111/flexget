import structure
import yaml

with open(structure.path, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
    print cfg['templates']['tv']['series']['settings']['default']['quality']
    