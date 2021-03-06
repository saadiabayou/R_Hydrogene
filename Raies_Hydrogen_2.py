# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:52:33 2020

@author: Saadia Bayou
"""
# données
evJ=1.6076634e-19 # Joules -> 1 electronvolt vaut 1,6076634.10e-19 Joules
RH=1.10e7 # RH = 1.10e7 m-1
h=6.63e-34 # h = 6.63e-34 m2.kg.s-1
c=3.00e8 # c=3.00e08 m.s-1  
lambdas=[]
Energies=[]

#metre -> nanometre
def convert_m_nm (l):
    """Convertit une grandeur en mètre en nanomètre"""
    L=l*(1e+09)
    return L
# nanometre -> metre
def convert_nm_m(l):
    """ Convertit une grandeur en nanomètre en mètre """
    L=l/(1e+09)
    return L

def convert_Jev (EJ):
    """ Cette fonction convertit une grandeur de Joule à electronVolt"""
    return EJ/evJ 

n=list(range(1,8)) # liste de nombre quantique du 1er niveau au niveau 7 

def Raie_Hydrogen(n):
    
    for i in range(len(n)):
        
        n1=n[i]
        print("\nn1=", n1)
        if n1==1:
            print ("Serie de Lyman")
        elif n1==2:
            print("Serie de Balmer")
        elif n1==3:
             print("Serie de Paschen")
        elif n1==4:
             print("Serie de Bracket")
        elif n1==5:
             print("Serie de Pfund")
        else:
            print("Serie de Humphreys")
        
        ln2=n[n1:n[-1]]
        print("la liste des  niveaux n2 est : liste_n2 =",ln2)
        
        for n2 in ln2:
            
            lambd=1/(RH*((1/(n1**2))-(1/(n2**2))))
            E=(h*c)/lambd
            E=convert_Jev(E)
            E=round(E,2)
            lambd=convert_m_nm (lambd)
            lambd=round(lambd,2)  
            print("\nAu niveau d'énergie n2 =",n2,", la longueur d'onde lambda(",n2,")=",lambd,"nm")
            print("et l'énergie de transition correspondante est E(",n2,")=",E,"ev")
            lambdas.append(lambd)
            Energies.append(E)

print(Raie_Hydrogen(n))


