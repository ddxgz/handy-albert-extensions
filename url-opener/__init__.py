#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""This is a simple python template extension.

This extension should show the API in a comprehensible way. Use the module docstring to provide a \
description of the extension. The docstring should have three paragraphs: A brief description in \
the first line, an optional elaborate description of the plugin, and finally the synopsis of the \
extension.

Synopsis: <trigger> [delay|throw] <query>"""

import json
import re

from albertv0 import *
import os
from time import sleep


__iid__ = "PythonInterface/v0.1"
__prettyname__ = "UrlOpener"
__version__ = "1.0"
__trigger__ = "u "
__author__ = "Cong Peng"
__dependencies__ = ["whatever"]

iconPath = iconLookup("albert")

config_filename = "urls.json"
config_file = os.path.join(
    os.path.join(configLocation(), __prettyname__),
    config_filename
)

url_pairs = {
    "twitter": "https://twitter.com"
}

# Can be omitted
def initialize():
    if os.path.exists(config_file):
        with open(config_file) as json_config:
            url_pairs.update(json.load(json_config))


# Can be omitted
def finalize():
    pass


def handleQuery(query):
    if not query.isTriggered:
        return

    results = []

    item = Item()

    item.icon = iconPath
    item.text = 'To open URL for %s' % query.string

    for k, v in url_pairs.items():
        if re.search(query.string.strip(), k, re.IGNORECASE):
            item = Item(id=__prettyname__,
                        icon=os.path.dirname(__file__)+"/plugin.png",
                        text=k,
                        subtext=v,
                        completion=__trigger__ + k,
                        urgency=ItemBase.Alert,
                        actions=[
                            UrlAction(text="UrlAction",
                                    url=v)
                        ])
            results.append(item)

    return results
