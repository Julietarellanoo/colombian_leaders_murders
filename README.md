# Visualization on a 3D web map of the number of homicides of social leaders in Colombia

The objective is to compile open source geographic data in order to highlight the information linked to the number of murders by region in Colombia and visualize them in 3D.

## Methodological scheme

![Sheme](https://github.com/Julietarellanoo/colombian_leaders_murders/blob/master/images/meto_final.PNG)

## The Data and Sources d’acquisition

* Collection of csv files from different NGOs and own adaptation  https://somosdefensores.org/
* Csv file of the Dead by socio-political violence                https://www.datos.gov.co/
* Administrative boundaries of the Colombian regions              https://data.humdata.org/dataset/colombia-administrative-bonduries-levels-0-3          

## Built With

* [kepler](https://kepler.gl/#/) - The WebMap app
* Python - Programming language

## What's Kepler?
[Kepler.gl](https://kepler.gl/#/) is a Uber’s Open Source Geospatial Toolbox for large-scale data sets. Built on top of the [deck](https://deck.gl/#/) WebGL data visualization framework, kepler.gl scales the map creation process by quickly gaining insights and validating visualization ideas from geospatial data.


## Authors

* **Julieth Arellano** - *student* - [Julietarellanoo](https://github.com/Julietarellanoo)

## Contributions

* **Pierre Bails** - *Professor* - [Baipi](https://github.com/baipi)

## Results

Source: kepler.gl 
* [link final work](https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/8y8p1z3r3hxftux/keplergl_rmfxir5.json)

![kepler.gl](https://github.com/Julietarellanoo/colombian_leaders_murders/blob/master/images/kepler.PNG)


## Challenges
* The initial objective of developping the webmapping process from the beginning to the end encountered obstacles because of difficulties in the administration of my personnal time, my learning curve which is a bit slow, and the apparition of new learning challenges with the beginning of my internship. However, the discovery of developpers' tools (kepler), allowed me to realize a 3D web cartography of an important latinoamerican social phenomenon.


## Recommendations for improve
* Implementation the automatic test for debugging in leaders.py
* More custumer options using deck.gl instead of kepler toolbox
