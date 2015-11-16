import structure
import save
import os.path

if not os.path.isfile(structure.path):
    save.saveConfig(structure.default)