python is the directory in which the information necessary for the creation of the geojson for the visualization of the web map is stored.

| Directory | Content |
| ------ | ------ |
| Data | csv file and boundaries_colombia geoJSON  |
| jupyter_notebook | Notebook_leaders [script python]  |
| output | csv file and final geoJSON |

# Python Script

## Use with Python

Run:
```
python3 leaders.py 
```
Result will be stored in `output` folder

## Use with Docker
[Doc](https://runnable.com/docker/python/dockerize-your-python-application)

## What is Docker

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.

Build:
```
docker build -t python-leaders_murdered .
```

Run:
```
docker run -it --rm -v $(pwd)/output:/output python-leaders_murdered
```

Result will be stored in `output` folder
