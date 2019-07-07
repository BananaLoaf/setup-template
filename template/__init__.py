PAYLOAD = {
    "name": "template",
    "version": "1.0",
    "license": "MIT",
    "install_requires": None,
    "packages": ("template", ),  # Better to be done by hand
    "entry_points": {
        "console_scripts": [
            "template = template.main:main",
            "template-again = template.main:main"
        ],
        "gui_scripts": [
            "template = template.main:main"
        ]
    },

    # Metadata for PyPi
    "author": "BananaLoaf",
    "author_email": "bananaloaf@protonmail.com",
    "description": None,
    "long_description": None,
    "long_description_content_type": "text/markdown",
    "keywords": ["template", "whatever"],
    "url": "https://github.com/BananaLoaf/template",
    "project_urls": {
        "Setup docs": "https://docs.python.org/2/distutils/setupscript.html",
        "Classifiers": "https://pypi.org/classifiers/"
    },
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
}