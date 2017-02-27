import os
import sys
import NatronEngine

def dirmap(app):
    table = app.projectPaths.getTable()
    for i in table:
        if table[i][0] == "MyFiles":
            if NatronEngine.natron.isLinux():
                table[i][1] = "...."
            elif NatronEngine.natron.isWindows():
                table[i][1] = "...."
           break
     app.projectPaths.setTable(table)


NatronEngine.natron.setOnProjectLoadedCallback("dirmap")
