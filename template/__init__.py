from setuptools import find_packages

__version__ = "1.0"


PAYLOAD = {
    "name": None,
    "version": __version__,
    "install_requires": None,
    "packages": find_packages(),
    "entry_points": {
        "console_scripts": [
            "template = template.main:main TEMPLATE",
            "template-again = template.main:main TEMPLATE"
        ],
        "gui_scripts": [
            "template = template.main:main TEMPLATE"
        ]
    },

    # Metadata for PyPi
    "author": "BananaLoaf",
    "author_email": "bananaloaf@protonmail.com",
    "maintainer": "BananaLoaf",
    "maintainer_email": "bananaloaf@protonmail.com",
    "license": None,

    "description": "This line is a description",
    "long_description": None,
    "long_description_content_type": "text/markdown",
    "keywords": ["template TEMPLATE", "whatever TEMPLATE"],

    "url": "https://github.com/BananaLoaf/template TEMPLATE",
    "download_url": None,
    "project_urls": {
        "Setup docs TEMPLATE": "https://docs.python.org/2/distutils/setupscript.html TEMPLATE",
        "Classifiers TEMPLATE": "https://pypi.org/classifiers/ TEMPLATE"
    },

    "classifiers": [
        "Development Status :: 5 - Production/Stable TEMPLATE",
        "Programming Language :: Python :: 3 TEMPLATE",
        "License :: OSI Approved :: MIT License TEMPLATE",
        "Operating System :: OS Independent TEMPLATE"
    ]
}
