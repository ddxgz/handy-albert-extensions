#!/usr/bin/env python3

"""List and open your Atom projects.
Synopsis: <trigger> [filter]"""

import os
import re
import time
from datetime import datetime
from pathlib import Path
from shutil import which

# import cson

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Quick Note"
__version__ = "1.0"
__trigger__ = "qn "
__author__ = "Cong Peng"
# __dependencies__ = ["python-cson"]

notefile = str(Path.home()) + "/Dropbox/Textnotes/quicknote.org"
iconPath = iconLookup('text-editor')


def handleQuery(query):
    if not query.isTriggered:
        return

    notes = query.string

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S%z")

    notes = f'\n<{timestamp}>\n{notes}\n'
    info(notes)


    def appendnote():
        with open(notefile, "a") as myfile:
            myfile.write(notes)

    items = []
    items.append(Item(id=__prettyname__,
                        icon=iconPath,
                        text=f"Add to quicknote.org",
                        # subtext=f'{projects_file}/{project}',
                        completion=query.rawString,
                        actions=[
                            FuncAction(text="call fn to append", callable=appendnote)
                            ]))

    return items
