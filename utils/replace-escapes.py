#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

replacements = (
    ("\\\"{a}", "ä"),
    ("\\\"{o}", "ö"),
    ("\\\"{u}", "ü"),
    ("\\\"{A}", "Ä"),
    ("\\\"{O}", "Ö"),
    ("\\\"{U}", "Ü"),
    ("\\\"a", "ä"),
    ("\\\"o", "ö"),
    ("\\\"u", "ü"),
    ("\\\"A", "Ä"),
    ("\\\"O", "Ö"),
    ("\\\"U", "Ü"),
    ("\\ss{}", "ß"),
    ("{\\ss}", "ß")
)

import fileinput
for line in fileinput.input():
    for fromStr, toStr in replacements:
        line = line.replace(fromStr, toStr)
    print line,
