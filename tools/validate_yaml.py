#!/usr/bin/python

import os
import sys
import yaml

YAML_DIR = "%s/../host_vars/" % os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(YAML_DIR):
    yaml_file = "%s%s" % (YAML_DIR, filename)

    if os.path.isfile(yaml_file) and ".yml" in yaml_file:
        try:
            with open(yaml_file) as yamlfile:
                configdata = yaml.load(yamlfile)
        except Exception:
            print("%s failed YAML import" % yaml_file)
            sys.exit(1)

sys.exit(0)
