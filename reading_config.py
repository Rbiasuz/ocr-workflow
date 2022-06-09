
import json 

with open('config', 'r') as f:
    config = json.load(f)

groups = config.keys()

config['emails']['key']
config['emails']['folder']