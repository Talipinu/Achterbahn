# -*- coding: iso-8859-1 -*-

'''
Created on 14.01.2018

@author: Stefan Goerig
'''

from math import sin, cos, pi
import matplotlib.pyplot as plt


# Bahnparameter

l1 = 20     # Länge des Bahnstücks 1
phi1 = -30  # Winkel des Bahnstücks 1

r2 = 10     # Radius des Bahnstücks 2

l3 = 20     # Länge des Bahnstücks 3
phi3 = 30   # Winkel des Bahnstücks 3

r4 = 10     # Radius des Bahnstücks 4

l5 = 20     # Länge des Bahnstücks 5
phi5 = -60  # Winkel des Bahnstücks 5

r6 = 10     # Radius 6

l7 = 20     # Länge des Bahnstücks 7


# Fahrzeugparameter
m = 300     # Masse des Wagens
cW = 1.3    # cW-Wert des Wagens
A = 1.2     # Stirnfläche des Wagens [m²]

v0 = 0          # Startgeschwindigkeit


# Umgebungsparameter
rhoLuft = 1.3    # Dichte der Luft [kg/dm³]


# Simulationsparameter
zSW = 1   # Zeitschrittweite 


# Plotparameter
pSW = 1    # Plotschrittweite



if __name__ == '__main__':
    
    # Berechnung der Vektoren der Anschlussstellen
    pStütz = [[], []]   # Liste der Stützvektoren
    pBahn = [[], []]     # Liste der Streckenvektoren (zum Zeichnen der Bahn)
   
    
    # Geradenstück 1
    # Stützvektor des Geradenanfangs berechnen
    pStütz[0].append(0)
    pStütz[1].append(0)
           
    # Stützvektor des Geradenendes berechnen
    pStütz[0].append(pStütz[0][-1] + l1 * cos(phi1 / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + l1 * sin(phi1 / 180 * pi))
    
    # Streckenvektoren der Geradenbahn berechnen    
    for i in range(0, l1 * pSW):
        pBahn[0].append(i / pSW * cos(phi1 / 180 * pi))
        pBahn[1].append(i / pSW * sin(phi1 / 180 * pi))    
    
    
    # Kreisstück 2
    # Stützvektor des Kreisbahnmittelpunkts berechnen
    phi2a = phi1 + 90 
    pStütz[0].append(pStütz[0][-1] + r2 * cos(phi2a / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r2 * sin(phi2a / 180 * pi))
    
    # Stützvektor des Kreisbahnendes berechnen
    phi2b = phi3 + 270 
    pStütz[0].append(pStütz[0][-1] + r2 * cos(phi2b / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r2 * sin(phi2b / 180 * pi))

    # Streckenvektoren der Kreisbahn berechnen    
    for i in range(phi2a, phi2b + 360, 5):
        pBahn[0].append(pStütz[0][2] + r2 * cos(i / 180 * pi))
        pBahn[1].append(pStütz[1][2] + r2 * sin(i / 180 * pi))
    
    
    # Geradenstück 3
    # Stützvektor des Geradenanfangs = Stützvektor des Kreisbahnendes
        
    # Stützvektor des Geradenendes berechnen
    pStütz[0].append(pStütz[0][-1] + l3 * cos(phi3 / 180 * pi))
    pStütz[1].append(pStütz[1][-1]+ l3 * sin(phi3 / 180 * pi))
    
    # Streckenvektoren berechnen    
    for i in range(0, l3 * pSW):
        pBahn[0].append(pStütz[0][-2] + i / pSW * cos(phi3 / 180 * pi))
        pBahn[1].append(pStütz[1][-2] + i / pSW * sin(phi3 / 180 * pi))    

    
    # Kreisstück 4 
    # Zentrum Kreis 4
    phi4a = phi3 - 90 
    
    # Stützvektor des Kreismittelpunkts berechnen
    pStütz[0].append(pStütz[0][-1] + r4 * cos(phi4a / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r4 * sin(phi4a / 180 * pi))
    
    # Austrittswinkel des Kreisbahnendes berechnen
    phi4b = phi5 + 90 
    
    # Stützvektor des Kreisbahnendes berechnen
    pStütz[0].append(pStütz[0][-1] + r4 * cos(phi4b / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r4 * sin(phi4b / 180 * pi))

    # Streckenvektoren der Kreisbahn berechnen    
    for i in range(phi4a + 90, phi4b + 90, 5):
        pBahn[0].append(pStütz[0][-2] + r4 * cos(i / 180 * pi))
        pBahn[1].append(pStütz[1][-2] + r4 * sin(i / 180 * pi))
    
    # Gerade 5
    # Stützvektor des Geradenanfangs = Stützvektor des Kreisbahnendes
        
    # Stützvektor des Geradenendes berechnen
    pStütz[0].append(pStütz[0][-1] + l5 * cos(phi5 / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + l5 * sin(phi5 / 180 * pi))
    
    # Streckenvektoren berechnen    
    for i in range(0, l5 * pSW):
        pBahn[0].append(pStütz[0][-2] + i / pSW * cos(phi5 / 180 * pi))
        pBahn[1].append(pStütz[1][-2] + i / pSW * sin(phi5 / 180 * pi))    

    # Kreisstück 6 
    # Stützvektor des Kreismittelpunkts berechnen
    phi6a = phi5 + 90 
    pStütz[0].append(pStütz[0][-1] + r6 * cos(phi6a / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r6 * sin(phi6a / 180 * pi))
    
    # Stützvektor des Kreisbahnendes berechnen
    phi6b = - 90 
    pStütz[0].append(pStütz[0][-1] + r6 * cos(phi6b / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r6 * sin(phi6b / 180 * pi))

    # Streckenvektoren der Kreisbahn berechnen    
    for i in range(phi6a + 180, phi6b + 360, 5):
        pBahn[0].append(pStütz[0][-2] + r6 * cos(i / 180 * pi))
        pBahn[1].append(pStütz[1][-2] + r6 * sin(i / 180 * pi))

    # Gerade 7
    # Stützvektor des Geradenanfangs 7 = Stützvektor des Kreisbahnendes 6
        
    # Stützvektor des Geradenendes berechnen
    pStütz[0].append(pStütz[0][-1] + l7)
    pStütz[1].append(pStütz[1][-1])
    
    # Streckenvektoren berechnen    
    for i in range(0, l5 * pSW):
        pBahn[0].append(pStütz[0][-2] + i / pSW)
        pBahn[1].append(pStütz[1][-2])    
    
    print (pStütz)
    
    
    # Fenster ausgeben
    plt.axes().set_aspect('equal', 'datalim')
    plt.plot(pBahn[0], pBahn[1], 'g.')
    plt.plot(pStütz[0], pStütz[1], 'bx')
    
    plt.arrow(0, 0, 10, 20, head_width=1, head_length=2, fc='k', ec='k')
    
    plt.show()