from collections import ChainMap
defaults = {"timeout": 30, "debug": False}
environment = {"timeout": 15}
runtime = {"debug": True}
config = ChainMap(runtime, environment, defaults)
print(config["timeout"])
print(config["debug"])
defaults["timeout"] = 60
print(config["timeout"])
