"""
Exercise C4 — Layered Configuration
Build layered_config.py.

Requirements:
- Define default, environment, and runtime configuration dictionaries.
- Combine them with ChainMap in the correct priority order.
- Demonstrate values inherited from lower-priority mappings.
- Show that a higher-priority value overrides a lower-priority value.
- Explain whether changing an underlying dictionary affects the ChainMap lookup.

"""


from collections import ChainMap


# 1. Low Priority: Base configurations used if nothing else is specified.
default_config = {
    "port": 8080,
    "debug": False,
    "theme": "light",
    "timeout": 30
}

# 2. Medium Priority: Configurations typically set via shell variables or OS flags.
environment_config = {
    "port": 9000,          # Overrides default_config["port"]
    "debug": True          # Overrides default_config["debug"]
}

# 3. High Priority: Temporary tweaks injected at command runtime.
runtime_config = {
    "port": 5000           # Overrides both environment and default ports!
}


config_pipeline = ChainMap(runtime_config,environment_config,default_config)



print(config_pipeline["port"])
print(config_pipeline["debug"])

print(config_pipeline["timeout"])  # Before change

default_config["timeout"] = 60

print(config_pipeline["timeout"])  # After change


# Explain whether changing an underlying dictionary affects the ChainMap lookup

# Ans: Yes

# The ChainMap doesnt create a copy of the dictionaries. instead it stores the references to the actual underlying dictionary objects.• If we change a value inside environment_config or default_config later in the script, that change will be reflected immediately inside our ChainMap lookups.

