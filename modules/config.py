import yaml

with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

config.update(config)

# statsdactyl
title = config['title']
port = config['port']
debug = config['debug']
alert = config['alert']
panel_url = config['panel_url']
api_key = config['api_key']
