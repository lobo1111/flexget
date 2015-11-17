import structure
import yaml

with open(structure.path, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
    for serie in cfg['templates']['tv']['series']['default']:
        print serie
    