# Visualization on a 3D web map of the number of homicides of social leaders in Colombia

The objective is to compile open source geographic data in order to highlight the information linked to the number of murders of social leaders by region in Colombia and visualize them in 3D.

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

## The 3 key points of kepler.gl:
* Ease of building data visualizations on interactive maps on the web, on a designed platform with a comfortable user experience.
*  The commitment to Open Source, being supported by large corporations such as Uber and Mapbox.
*  Integration with other products and platforms frome third parties such as CARTO, and with frameworks JavaScript such as React to integrate the map into an app as one of its component. 

As a summary, kepler.gl is a tool made up of a platform to build geographic information visualizations quickly, easily, intuitively, with good graphic results and great interaction with the user.

## Using kepler to visualize the leaders assassinated in Colombia in 2019
1. Load the generated geoJSON from **leaders.py**.
```sh
$ python3 leaders.py
```
2.   Add layer **result.geoJSON** and symbolize it.
![kepler.gl](https://github.com/Julietarellanoo/colombian_leaders_murders/blob/master/images/tableau.png)


## Which selection parametres in Kepler?
The choice of the parameters was realized regarding :
* The geoJSON properties (number of "Morts") as a 3D volume inside the map allows a better visualization of the quantity of homicides in relation to a volume instead of to a number, this helps a lot in the hierarchisation of the phenomenon.
* A thematic and sequential range of colors (reds and oranges) that helps to do a follow up of the evolution of the social problem, from the less affected departments to the most impacted ones.
* Height for each polygone depending on the quantity of homicides in order to highlight the most affected departments. 
* The choice of the Map template style in Mapbox was "light". The template offers a subtle light backdrop for data visualizations, creating an harmony with the quite dense color range of the 3D map. 

## Why 3D web Map?

The 3D web maps are tools for the visualization of three-dimensional data (3D) that allow the user to view the information from new points of view. 3D maps allow the exploration of perspectives which possibly could not be visualizable on conventional bidimensional maps and charts (2D). The use of online cartographic tools allows the user to interact with the information and so to appropriate it more easily.   

The challenges are, on one hand, to lighten the formats (geoJSON) using GIS tools and programmation languages like Python to reduce the waiting times of the user, and on the other hand, to turn the maps into an attractive and interactive communication tool.

3. Apply filter and interaction options.
![kepler.gl](https://github.com/Julietarellanoo/colombian_leaders_murders/blob/master/images/filter.png)
![kepler.gl](https://github.com/Julietarellanoo/colombian_leaders_murders/blob/master/images/interactions.png)

4. Export and share data and map.
![kepler.gl](https://github.com/Julietarellanoo/colombian_leaders_murders/blob/master/images/share.png)

**Final work in Results**
## Author

* **Julieth Arellano** - *student* - [Julietarellanoo](https://github.com/Julietarellanoo)

## Contributions

* **Pierre Bails** - *Professor* - [Baipi](https://github.com/baipi)

## Results

Source: kepler.gl 
* [link final work](https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/fnris2rqj4glub6/keplergl_bojdsai.json)

![kepler.gl](https://github.com/Julietarellanoo/colombian_leaders_murders/blob/master/images/webcarte.png)


## Challenges
* The initial objective of developping the webmapping process from beginning to end encountered obstacles because of difficulties in the administration of my personnal time, my learning curve which is a bit slow, and the apparition of new learning challenges with the beginning of my internship. However, the discovery of developpers' tools (kepler), allowed me to realize a 3D web cartography of an important latinoamerican social phenomenon.


## Recommendations for further improvement
* Implementation of the automatic test for debugging in leaders.py
* Inclusion of more user options using deck.gl instead of kepler toolbox
* Implementation of Real-time data analysis
