try:
    from setuptools import setup
except ModuleNotFoundError:
    from distutils.core import setup

from template import PAYLOAD


with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()
description = LONG_DESCRIPTION.split("\n")[1]

PAYLOAD["description"] = LONG_DESCRIPTION.split("\n")[1]
PAYLOAD["long_description"] = LONG_DESCRIPTION
PAYLOAD["install_requires"] = ["numpy", ]  # Same as requirements.txt


payload = {}
for key in PAYLOAD:
    if PAYLOAD[key]:
        payload[key] = PAYLOAD[key]


setup(**payload)
