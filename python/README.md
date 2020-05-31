# Python Script

## Use with Python

Run:
```
python leaders.py 
```
Result will be stored in `output` folder

## Use with Docker
[Doc](https://runnable.com/docker/python/dockerize-your-python-application)

Build:
```
docker build -t python-leaders_murdered .
```

Run:
```
docker run -it --rm -v $(pwd)/output:/output python-leaders_murdered
```

Result will be stored in `output` folder
