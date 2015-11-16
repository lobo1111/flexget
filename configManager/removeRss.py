import structure
import sys
import yaml
import save

with open(structure.path, 'rw') as ymlfile:
    cfg = yaml.load(ymlfile)
    del cfg['tasks'][sys.argv[1]]
    save.saveConfig(cfg)
    