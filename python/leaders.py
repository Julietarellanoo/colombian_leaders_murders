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
import json
import os



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

def leadersmorts_dpt(source):
    """
    Compte le nombre de homicides par departement et renvoie
    une liste de dictionnaires.
    """

    with open(source,encoding="utf-8",mode="r") as file:
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

def addproperties_json(source, mortspd):
    """
    Adition de nombre de leaders morts par departement au geojson
    """
    with open(source, encoding="utf-8",mode="r") as f: # load boundaries
     boundaries = json.load(f)
     

    for regionBoundary in boundaries['features']: # get nb murdered by region
        del regionBoundary['properties']['admin1Pcod']
        del regionBoundary['properties']['admin1RefN']
        
        regionBoundary['properties']['Departement'] = regionBoundary['properties']['admin1Name']
        
        currentRegion = regionBoundary['properties']['Departement']
        if currentRegion in mortspd:
            regionBoundary['properties']['Morts'] = mortspd[currentRegion]
            
        else: 
            regionBoundary['properties']['Morts'] = 0                
            continue
    return  boundaries

def main():
    print("********************************")
    print("* Geocoding *")
    print("********************************")
    print("\n")

    print(" - import des données...")
    source = "./data/lideres_asesinados.csv"    
    leaders = leadersmorts_dpt(source)
    print("   ... {} départements recensés avec 1 ou plus meurtres".format(len(leaders)))
    
    boundariesFilePath = "./data/boundaries_colombia.geojson" 
    boundariesWithCount = addproperties_json(boundariesFilePath, leaders)

    if not os.path.exists("output"):
        os.makedirs("output")
    boundariesWithCountFile = open("./output/result.geojson",mode= "w", encoding="utf-8")
    boundariesWithCountFile.write(json.dumps(boundariesWithCount))
    boundariesWithCountFile.close()


if __name__ == "__main__":
    main()