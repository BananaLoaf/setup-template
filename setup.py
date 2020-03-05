try:
    from setuptools import setup
except ModuleNotFoundError:
    from distutils.core import setup

from template import PAYLOAD


with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()
PAYLOAD["long_description"] = LONG_DESCRIPTION


import json
assert PAYLOAD["description"] == "This line is a description"
assert json.dumps(PAYLOAD).find("TEMPLATE") == -1
assert json.dumps(PAYLOAD).find("null") == -1


kwargs = {}
for key in PAYLOAD:
    if PAYLOAD[key] is not None:
        kwargs[key] = PAYLOAD[key]

setup(**kwargs)
