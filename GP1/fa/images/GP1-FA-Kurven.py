#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# Dieses Python-Skript war die Grundlage zur Neuerstellung der Grafik GP1-FA-Kurven. Ähnliche Ergebnisse konnten mit normalen Plottingprogrammen wie OpenOffice.org Draw oder QtiPlot nicht erzielt werden, da diese kein Wahrscheinlichkeitsnetz zeichnen können.
# Dieses Skript verwendet matplotlib, in dem Umfang, den ich während der Computational-Physics-Lehrveranstaltung erlernt habe. Falls Sie diese Grafik bearbeiten wollen, aber kein Python können: Bei Herrn Dr. Bäcker bzw. allgemein beim Lehrstuhl Computational Physics gibt es gute Einführungsdokumente.

from pylab import *
from scipy.special import erf

################################################################################
### Konstanten und Hilfsfunktionen

# Parameter unserer Wahrscheinlichkeitsverteilung
mu = 10.0
sigma = 2.0

# Wahrscheinlichkeitsverteilung
def W(x):
	return exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sqrt(2 * pi) * sigma)

# Summenkurve (erf ist die Gauss-Fehlerfunktion)
def S(x):
	xNormal = (x - mu) / (sqrt(2) * sigma)
	return (1 + erf(xNormal)) / 2

# eine Rundungs-Funktion, die auf Arrays operiert
def around(array, ndigits):
	roundFunctor = lambda number: round(number, ndigits)
	return map(roundFunctor, array)

################################################################################
### Plotten der Grafiken (Die dritte heben wir uns bis zum Schluss auf, denn sie ist die schwerste.)

figure(0, figsize=(10, 3))

# erste und zweite Grafik: Gaußsche Glockenkurve
xArray = linspace(5, 15, 200)
WArray = W(xArray)
SArray = S(xArray)

subplot(141, autoscale_on=False)
axis([5, 15, 0, 0.2])
xlabel("Messgroesse x") # Leider sind in Labels keine Umlaute möglich.
ylabel("W(x)")
plot(xArray, WArray)

subplot(142, autoscale_on=False)
axis([5, 15, 0, 1])
xlabel("Messgroesse x")
ylabel("S(x)")
plot(xArray, SArray)

# vierte Grafik: logarithmierte Häufigkeitskurve
subplot(144, autoscale_on=False, yscale="log")
axis([0, 25, 8E-3, 2.5E-1])
xlabel("(x-10)^2")
ylabel("W(x)")
plot((xArray - mu) ** 2, WArray)

# dritte Grafik: Wahrscheinlichkeitsnetz
yMetaArray = linspace(0, 1, len(xArray))

ax = subplot(143, autoscale_on=False)
axis([5, 15, 0, 1])
xlabel("Messgroesse x")
ylabel("S(x)")
plot(xArray, yMetaArray)

# Das ist der ganze Trick: Wir haben jetzt nicht S(x), sondern eine Gerade geplottet. Das ist das, was im Wahrscheinlichkeitsnetz auch für die Gauss-Summenverteilung rauskommen würde. Damit das ganze authentisch aussieht, müssen wir nur noch die Achsenbeschriftungen anpassen. :-)
yAxis = ax.get_yaxis()
# Zunächst setzen wir die Markierungen auf der Y-Achse an ganz bestimmte Stellen, die auf der X-Achse den natürlichen Zahlen von 5 bis 15 entsprechen. (Achtung: Dies sind nicht zehn, sondern elf Zahlen!)
yTicksArray = linspace(0, 1, 11)
yAxis.set_ticks(yTicksArray)
# Nun setzen wir auf die passenden Beschriftungen, indem wir S an den entsprechenden x-Positionen ausrechnen.
xTicksArray = linspace(5, 15, 11)
STicksArray = S(xTicksArray)
yAxis.set_ticklabels(around(STicksArray, 3))

# Grafiken anzeigen
show()
