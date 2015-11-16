import structure
import yaml

def saveConfig(config):
    with open(structure.path, 'w') as outfile:
        outfile.write(yaml.dump(config, default_flow_style=True))