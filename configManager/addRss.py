import structure
import sys
import yaml
import save

with open(structure.path, 'rw') as ymlfile:
    cfg = yaml.load(ymlfile)
    cfg['tasks'][sys.argv[1]] = dict(
            template = "tv",
            rss = sys.argv[2]
        )
    save.saveConfig(cfg)
    