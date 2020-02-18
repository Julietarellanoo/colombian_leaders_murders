# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 13:50:51 2020

@author: Julieta_Montesco

Programme qui permet d'analyser un fichier cvs
(format ci-dessous) contenant les données des
leaders sociaux morts en Colombie pour assigner
les coordonnées(geocoding).

Exemple de fichier csv compatible :
id;Nombre;Género;Fecha;Municipio;Departamento;Tipo de líder;;;;;;;;;;;;;;;;;;
francisco-jaramillo-moreno;Francisco Jaramillo Moreno;M;2016-01-02;Briceño;Antioquia;Líder campesino o agrario;;;;;;;;;;;;;;;;;;
victor-jaramillo-moreno;Víctor Jaramillo Moreno;M;2016-01-02;Briceño;Antioquia;Líder campesino o agrario;;;;;;;;;;;;;;;;;;
willinton-andres-banol;Willinton Andres Bañol;M;2016-01-10;Pereira;Risaralda;Líder comunitario;;;;;;;;;;;;;;;;;;
mario-alexis-tarache;Mario Alexis Tarache Perez;M;2016-01-14;San Luis de Palenque;Casanare;Líder comunal;;;;;;;;;;;;;;;;;;

"""
import pandas as pd
import geopy
import geopandas as gpd
import matplotlib.pyplot as plt


def netoyer_donnees(l):
    """
    Transformer une liste de chaines de caractères
    en un dictionnaires.
    """
    d = {}
    d["id"] = l[0]    
    d["Nombre"] = l[1]
    d["Género"] = (l[2])
    d["Fecha"] = (l[3])
    d["Municipio"] = (l[4])
    d["Departamento"] = (l[5])
    d["Tipo de líder"] = (l[6])
    return d

def importer_donnees(fichier):
    """
    Importe un fichier csv et renvoie
    une liste de dictionnaires.
    """
       
    with open(fichier, "r") as file:
        leaders = []
        line = file.readline() # Lit la ligne d'entete
        
        for line in file:
            line = line.strip()
            if len(line) > 0:
                l = line.split(";")
                leader = netoyer_donnees(l)
                # requete geocode
                # mettre resultat dans le dico
                leaders.append(leader)
    print(leaders)
    return leaders


def main():
    print("********************************")
    print("* Geocoding *")
    print("********************************")
    print("\n")
    
    fichier = "Lideres_asesinados.csv"
    print(" - import des données...")
    leaders = importer_donnees(fichier)
    print("   ... {} données importés".format(len(leaders)))
    
main()