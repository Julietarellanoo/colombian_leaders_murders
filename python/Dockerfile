FROM python:3.7

ADD requirements.txt /
ADD data/Lideres_asesinados_short.csv /data/
ADD data/Lideres_asesinados.csv /data/
ADD data/boundaries_colombia.geojson /data/
ADD leaders.py /

RUN pip install -r requirements.txt

CMD [ "python", "./leaders.py" ]