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
from geopy.geocoders import Nominatim
import geopandas as gpd
import matplotlib.pyplot as plt
import json
#geolocator = Nominatim(user_agent="colombian_leaders_murders")


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
    
    #location = geolocator.geocode(d["Municipio"]+ " " + d["Departamento"]+" Colombia")
    
    #d["lat"] = location.latitude
    #d["lng"] = location.longitude
    return d

def leadersmorts_dpt(fichier):
    """
    Compte le nombre de homicides par departement et renvoie
    une liste de dictionnaires.
    """
       
    with open(fichier, "r") as file:
     nbmpd= {}
     line = file.readline() # Lit la ligne d'entete
     for line in file:
      line = line.strip()
      if len(line) > 0:
        l = line.split(";")
        leader = netoyer_donnees(l)

        # tri departements
        if leader["Departamento"]  in nbmpd:
            nbmpd[leader["Departamento"]] = nbmpd[leader["Departamento"]]+1
        else:
            nbmpd[leader["Departamento"]] = 1

    return nbmpd

def addproperties_json():
    """
    Adition de nombre de leaders morts par departement au geojson
    """

    boundaries = {}
    fichier = "Lideres_asesinados_short.csv"
    with open('boundaries_colombia.geojson', encoding="utf-8") as f:
     d = json.load(f)
    for item in d['features'][0]['properties']['admin1Name']:
        mortspd = leadersmorts_dpt(fichier)
        if mortspd["Departamento"] in boundaries:
            if boundaries[mortspd["Departamento"]] == d['features'][0]['properties']['admin1Name']:
                d['count'] = d['features'][0]['properties']['admin1Name'] + 1
            else:
                d['count'] = d['features'][0]['properties']['admin1Name'] + 1
    return  json          
       
def main():
    print("********************************")
    print("* Geocoding *")
    print("********************************")
    print("\n")
    
    fichier = "Lideres_asesinados_short.csv"
    print(" - import des données...")
    leaders = leadersmorts_dpt(fichier)
    print("   ... {} données importés".format(len(leaders)))
    json = addproperties_json()
    print("   ... {} données importés".format(len(json)))
main()