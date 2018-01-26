# -*- coding: iso-8859-1 -*-

'''
Created on 14.01.2018

@author: sagoe
'''

from math import sin, cos, pi
import matplotlib.pyplot as plt


''' Bahnparameter '''

l1 = 20     # Länge des Bahnstücks 1
phi1 = -60  # Winkel des Bahnstücks 1

r2 = 10     # Radius des Bahnstücks 2

l3 = 20     # Länge des Bahnstücks 3
phi3 = 30   # Winkel des Bahnstücks 3

r4 = 10     # Radius des Bahnstücks 4

l5 = 20     # Länge des Bahnstücks 5
phi5 = -60  # Winkel des Bahnstücks 5

r6 = 10     # Radius 6

l7 = 20     # Länge des Bahnstücks 7


''' Fahrzeugparameter '''

m = 300     # Masse des Wagens
cW = 1.3    # cW-Wert des Wagens
A = 1.2     # Stirnfläche des Wagens [m²]

v0 = 0          # Startgeschwindigkeit


''' Umgebungsparameter '''

rhoLuft = 1.3    # Dichte der Luft [kg/dm³]


''' Simulationsparameter '''

zSW = 1   # Zeitschrittweite 


''' Plotparameter '''

pSW = 1    # Plotschrittweite



if __name__ == '__main__':
    
    ''' Berechnung der Vektoren der Anschlussstellen '''
    
    pStütz = [[], []]   # Liste der Stützvektoren
    pAlle = [[], []]     # Liste der Streckenvektoren (zum Zeichnen der Bahn)
   
    
    ''' Geradenstück 1 '''
    # Stützvektor des Geradenanfangs berechnen
    pStütz[0].append(0)
    pStütz[1].append(0)
           
    # Stützvektor des Geradenendes berechnen
    pStütz[0].append(pStütz[0][-1] + l1 * cos(phi1 / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + l1 * sin(phi1 / 180 * pi))
    
    # Streckenvektoren der Geradenbahn berechnen    
    for i in range(0, l1 * pSW):
        pAlle[0].append(i / pSW * cos(phi1 / 180 * pi))
        pAlle[1].append(i / pSW * sin(phi1 / 180 * pi))    
    
    
    ''' Kreisstück 2 '''
       
    # Stützvektor des Kreisbahnmittelpunkts berechnen
    phi2a = phi1 - 90 
    pStütz[0].append(pStütz[0][-1] + r2 * cos(phi2a / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r2 * sin(phi2a / 180 * pi))
    
    # Stützvektor des Kreisbahnendes berechnen
    phi2b = phi3 + 90 
    pStütz[0].append(pStütz[0][-1] + r2 * cos(phi2b / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r2 * sin(phi2b / 180 * pi))

    # Streckenvektoren der Kreisbahn berechnen    
    for i in range(phi2a, phi2b + 360, 5):
        pAlle[0].append(pStütz[0][2] + r2 * cos(i / 180 * pi))
        pAlle[1].append(pStütz[1][2] + r2 * sin(i / 180 * pi))
    
    
    ''' Geradenstück 3 '''
    # Stützvektor des Geradenanfangs = Stützvektor des Kreisbahnendes
        
    # Stützvektor des Geradenendes berechnen
    pStütz[0].append(pStütz[0][-1] + l3 * cos(phi3 / 180 * pi))
    pStütz[1].append(pStütz[1][-1]+ l3 * sin(phi3 / 180 * pi))
    
    # Streckenvektoren berechnen    
    for i in range(0, l3 * pSW):
        pAlle[0].append(pStütz[0][-1] + cos(phi3) * i / pSW)
        pAlle[1].append(pStütz[1][-1] + sin(phi3) * i / pSW)    

    
    ''' Kreisstück 4 ''' 
    
    # Zentrum Kreis 4
    phi4a = phi3 - 90 
    
    # Stützvektor des Kreismittelpunkts berechnen
    pStütz[0].append(pStütz[0][-1] + r4 * cos(phi4a / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r4 * sin(phi4a / 180 * pi))
    
    # Austrittswinkel des Kreisbahnendes berechnen
    phi4b = phi5 - 90 
    
    # Stützvektor des Kreisbahnendes berechnen
    pStütz[0].append(pStütz[0][-1] + r4 * cos(phi4b / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r4 * sin(phi4b / 180 * pi))

    # Streckenvektoren der Kreisbahn berechnen    
    for i in range(phi4a, phi4b + 360, 5):
        pAlle[0].append(pStütz[0][5] + r4 * cos(i / 180 * pi))
        pAlle[1].append(pStütz[1][5] + r4 * sin(i / 180 * pi))
    
    
    ''' Gerade 5 '''
    
    # Stützvektor des Geradenanfangs = Stützvektor des Kreisbahnendes
        
    # Stützvektor des Geradenendes berechnen
    pStütz[0].append(pStütz[0][-1] + l5 * cos(phi5 / 180 * pi))
    pStütz[1].append(pStütz[1][-1]+ l5 * sin(phi5 / 180 * pi))
    
    # Streckenvektoren berechnen    
    for i in range(0, l5 * pSW):
        pAlle[0].append(pStütz[0][-1] + cos(phi5) * i / pSW)
        pAlle[1].append(pStütz[1][-1] + sin(phi5) * i / pSW)    

    
    ''' Kreisstück 6 ''' 
    
    
    # Stützvektor des Kreismittelpunkts berechnen
    phi6a = phi5 - 90 
    pStütz[0].append(pStütz[0][-1] + r6 * cos(phi6a / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r6 * sin(phi6a / 180 * pi))
    
    # Stützvektor des Kreisbahnendes berechnen
    phi6b = -90 
    pStütz[0].append(pStütz[0][-1] + r6 * cos(phi6b / 180 * pi))
    pStütz[1].append(pStütz[1][-1] + r6 * sin(phi6b / 180 * pi))

    # Streckenvektoren der Kreisbahn berechnen    
    for i in range(phi6a, phi6b, 5):
        pAlle[0].append(pStütz[0][-2] + r6 * cos(i / 180 * pi))
        pAlle[1].append(pStütz[1][-2] + r6 * sin(i / 180 * pi))
    
    
    ''' Gerade 7 '''
    # Stützvektor des Geradenanfangs 7 = Stützvektor des Kreisbahnendes 6
        
    # Stützvektor des Geradenendes berechnen
    pStütz[0].append(pStütz[0][-1] + l7)
    pStütz[1].append(pStütz[1][-1])
    
    # Streckenvektoren berechnen    
    for i in range(0, l5 * pSW):
        pAlle[0].append(pStütz[0][-1] + i / pSW)
        pAlle[1].append(pStütz[1][-1])    
    

    ''' Fenster ausgeben'''
    
    print (pStütz[0])
    print (pStütz[1])
    print (pStütz)
    print (pAlle)
    
    plt.xlim(-30, 70)
    plt.ylim(-35, 30)
    plt.plot(pAlle[0], pAlle[1], 'ro')
    plt.plot(pStütz[0], pStütz[1], 'bx')
    plt.show()