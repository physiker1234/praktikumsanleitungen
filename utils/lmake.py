#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

IDENTIFICATION = "lmake 0.4"

# Aufrufsyntax: lmake [-i Installdir] [Pfad]
#
# Erstellt Makefiles im angegebenen Verzeichnis (inkl. automatischem Absteigen
# in Unterverzeichnisse, in denen TeX-Quellen liegen). Standard für den
# Basispfad ist ".", das aktuelle Arbeitsverzeichnis).
# Wenn -i angegeben wurde oder in ~/.lmakerc eine Zeile der Form
# "install_dir /mein/pfad" auftaucht, werden install-Targets erstellt.
#
# Es werden folgende Quelldateitypen erkannt:
#  *.tex
#  *.[dtx|ins]-Paare, sofern sie Dokumentklassen oder Pakete erstellen
# Beachte: Alle Makefiles sind in sich abgeschlossen, wenn man also in lmake in
# /a/b aufruft, kann man danach make auch in /a/b/c aufrufen, sofern dort ein
# Makefile erstellt wurde.
#
# Außerdem werden Dateien mit dem Namen "Makefile.in", sofern vorhanden, an das
# automatisch generierte Makefile angehangen.
# Achtung: Beim rekursiven Absteigen werden versteckte Ordner ignoriert.
# (Als versteckte Ordner werden solche mit einem Punkt am Anfang erkannt.)
#
# Die folgenden Spezial-Targets stehen in den erzeugten Makefiles bereit:
#  make install        (Sofern Installdir spezifiziert.) Kopiert die Kompilate
#                      (.pdf, .cls, .sty) in das Installdir.
#  make clean          Entfernt temp. Dateien, die beim Kompilieren anfallen.
#  make remove         Entfernt temp. Dateien sowie Kompilate.
#  make kill           Entfernt temp. Dateien, Kompilate und die Makefiles.
#
# Die folgenden Befehlszeilen in ~/.lmakerc werden erkannt:
#  install_dir [Pfad]  Setzt das Standard-Installationsverzeichnis.
#  install_includes    Wenn vorhanden, werden cls/sty-Dateien in die install-
#                      Regel eingeschlossen.
#

import sys, os, string
from fnmatch import fnmatch
from getopt import *

# .lmakerc auslesen
installDir = ""
installIncludes = False
try:
    rcpath = os.path.expanduser("~/.lmakerc")
    for line in open(rcpath):
        line = string.strip(line)
        if line[0:12] == "install_dir ":
            installDir = os.path.abspath(line[12:])
        elif line == "install_includes":
            installIncludes = True
except:
    pass
# Kommandozeile parsen
try:
    opts, args = getopt(sys.argv[1:], "i:")
except GetoptError, err:
    print str(err)
    print "Aufrufsyntax: lmake [-i Installdir] [Pfad]"
    print "Weitere Informationen siehe Quellcode."
    sys.exit(2)
# Arbeitsverzeichnis wählen
baseDir = "."
if len(args) > 1:
    if os.path.isdir(args[0]):
        baseDir = args[0]
    else:
        print "lmake: \"" + sys.argv[1] + "\" existiert nicht oder ist kein Verzeichnis."
        sys.exit(1)
# Installverzeichnis wählen
for option, value in opts:
    if option == "-i":
        installDir = os.path.abspath(value)

def joinPath(path, filename):
    return "/".join((path, filename))
def replaceExtension(path, extension):
    parts = path.split(".")
    parts[-1] = extension
    return ".".join(parts)

def process_dir(path, treeString = ""):
    ''' Rückgabewert: True, wenn ein Makefile erstellt wurde, sonst False '''
    clsSources = []
    stySources = []
    texSources = []
    subdirs = []
    hasCustomMakefile = False
    hasClsSources = False
    hasStySources = False
    hasTexSources = False
    hasSubdirs = False
    # schicke Ausgabe
    if path == baseDir:
        if path == ".":
            print treeString + os.getcwd()
        else:
            print treeString + baseDir
    else:
        print "/".join((treeString, os.path.basename(path)))
    # Suche nach Quelldateien und Unterverzeichnissen
    filenames = os.listdir(path)
    filenames.sort()
    for filename in filenames:
        filepath = joinPath(path, filename)
        # Dateien prüfen
        if os.path.isfile(filepath):
            if filename == "Makefile.in":
                hasCustomMakefile = True
            elif fnmatch(filepath, "*.tex"):
                texSources.append(filename)
                hasTexSources = True
            elif fnmatch(filepath, "*.ins"):
                dtxfile = replaceExtension(filepath, "dtx")
                if os.path.exists(dtxfile):
                    # Problem: dtx/ins -> was wird gebaut? (sty oder cls)
                    styfile = replaceExtension(filename, "sty")
                    clsfile = replaceExtension(filename, "cls")
                    for line in open(filepath):
                        if styfile in line:
                            stySources.append(styfile)
                            hasStySources = True
                            break
                        elif clsfile in line:
                            clsSources.append(clsfile)
                            hasClsSources = True
                            break
        # in Unterverzeichnisse absteigen (außer in versteckte)
        if os.path.isdir(filepath):
            if filename[0] != '.':
                if process_dir(filepath, treeString + "| "):
                    subdirs.append(filename)
                    hasSubdirs = True
    # Muss ein Makefile erstellt werden? - schicke Ausgabe, Teil 2
    buildMakefile = hasClsSources or hasStySources or hasTexSources or hasSubdirs or hasCustomMakefile
    if buildMakefile:
        message = "+-- Makefile"
    else:
        message = "+-- Skipping"
    if treeString == "":
        print message
    else:
        print treeString + message
    if not buildMakefile:
        return False
    # Makefile erstellen
    makefileLines = ["# Makefile autogenerated by " + IDENTIFICATION]
    ma = makefileLines.append
    # Variablen setzen
    ma("MYMAKEFLAGS = --silent")
    hasInstall = len(installDir) > 0
    if hasInstall:
        ma("INSTALLDIR = " + installDir)
    if hasSubdirs:
        ma("SUBDIRS = " + " ".join(subdirs))
    # Master-Regel hinzufügen
    allSources = clsSources + stySources + texSources
    pdfFiles = [replaceExtension(filename, "pdf") for filename in allSources]
    masterDeps = clsSources + stySources + pdfFiles
    if hasSubdirs:
        masterDeps.append("__LMAKE_SUBDIRS")
    ma(".PHONY: all")
    ma(" ".join(["all :"] + masterDeps))
    # generische Regeln hinzufügen
    if hasClsSources:
        ma("%.cls : %.ins %.dtx")
        ma("\tlatex $<")
        ma("%.pdf : %.dtx %.cls")
        ma("\tpdflatex $<")
        ma("\tpdflatex $<")
    if hasStySources:
        ma("%.sty : %.ins %.dtx")
        ma("\tlatex $<")
        ma("%.pdf : %.dtx %.sty")
        ma("\tpdflatex $<")
        ma("\tpdflatex $<")
    if hasTexSources:
        ma("%.pdf : %.tex")
        ma("\tpdflatex $<")
        ma("\tpdflatex $<")
    if hasSubdirs:
        ma(".PHONY: __LMAKE_SUBDIRS")
        ma("__LMAKE_SUBDIRS :")
        ma("\t@for i in $(SUBDIRS); do \\")
        ma("\t(cd $$i; make $(MFLAGS) $(MYMAKEFLAGS) all); done")
    # Install-Regel hinzufügen
    if hasInstall:
        ma(".PHONY: install")
        ma("install : all")
        ma("\t@mkdir -p $(INSTALLDIR)")
        if len(allSources) > 0:
            ma("\t@if test -d $(INSTALLDIR); then \\")
            if installIncludes:
                installFiles = pdfFiles + clsSources + stySources
            else:
                installFiles = pdfFiles
            for pdfFile in installFiles:
                ma("\t\tinstall -m 644 " + pdfFile + " $(INSTALLDIR); \\")
            ma("\tfi")
        if hasSubdirs:
            ma("\t@for i in $(SUBDIRS); do \\")
            ma("\t(cd $$i; make $(MFLAGS) $(MYMAKEFLAGS) install); done")
    # Clean-Regel hinzufügen
    ma(".PHONY: clean")
    ma("clean :")
    if hasStySources or hasClsSources or hasTexSources:
        ma("\t@rm -f *.aux *.bbl *.blg *.flg *.glo *.idx *.ind *.ilg *.lof *.log *.lot *.nav *.out *.snm *.toc *.vrb *.code.tmp")
    if hasSubdirs:
        ma("\t@for i in $(SUBDIRS); do \\")
        ma("\t(cd $$i; make $(MFLAGS) $(MYMAKEFLAGS) clean); done")
    # Remove-Regel hinzufügen
    ma(".PHONY: remove")
    ma("remove : clean")
    if hasStySources or hasClsSources or hasTexSources:
        ma(" ".join(["\t@rm -f"] + clsSources + stySources + pdfFiles))
    if hasSubdirs:
        ma("\t@for i in $(SUBDIRS); do \\")
        ma("\t(cd $$i; make $(MFLAGS) $(MYMAKEFLAGS) remove); done")
    # Kill-Regel hinzufügen
    ma(".PHONY: kill")
    ma("kill : remove")
    if hasSubdirs:
        ma("\t@for i in $(SUBDIRS); do \\")
        ma("\t(cd $$i; make $(MFLAGS) $(MYMAKEFLAGS) kill); done")
    ma("\t@rm -f Makefile")
    # Makefile schreiben
    ma("") # Leerzeilen am Ende von Textdateien sind unter Linux üblich
    makefilePath = joinPath(path, "Makefile")
    makefile = open(makefilePath, "w")
    try:
        makefile.write("\n".join(makefileLines))
        # benutzerdefiniertes Makefile
        if hasCustomMakefile:
            makefileInPath = joinPath(path, "Makefile.in")
            makefileIn = open(makefileInPath, "r")
            makefileInLines = ["# Custom makefile read from Makefile.in\n"]
            makefileInLines += makefileIn.readlines()
            makefile.write("".join(makefileInLines))
            makefileIn.close()
    except:
        print "ERROR: Failed to write", makefile
    finally:
        makefile.close()
    return True

process_dir(baseDir)
