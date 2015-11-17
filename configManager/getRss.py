import structure
import yaml

with open(structure.path, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
    for rss in cfg['tasks']:
        print rss.rss
    