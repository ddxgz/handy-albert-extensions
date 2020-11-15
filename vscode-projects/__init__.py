#!/usr/bin/env python3

"""List and open your Atom projects.
Synopsis: <trigger> [filter]"""

import os
import re
from pathlib import Path

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "VS Code Projects"
__version__ = "1.0"
__trigger__ = "code "
__author__ = "Cong Peng"

icon_path = iconLookup('inode-directory')
projects_file = str(Path.home()) + "/code"
projects = []


def handleQuery(query):
    if not query.isTriggered:
        return

    projects = os.listdir(projects_file)
    info(projects)

    stripped = query.string.strip()

    items = []
    for project in projects:
        if re.search(stripped, project, re.IGNORECASE):
            items.append(Item(id=__prettyname__,# + project,
                              icon=icon_path,
                              text=project,
                              subtext="Group",
                              completion=query.rawString,
                              actions=[
                                  ProcAction(text="Open project in VS Code",
                                             commandline=["code", project],
                                             cwd=projects_file)
                              ]))
    return items
