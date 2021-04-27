FROM python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /app

ADD . /app

RUN apt-get update
RUN apt-get install -y libproj-dev libgeos-dev gdal-bin
 
RUN pip install shapely --no-binary shapely

COPY ./requirements.txt /app/requirements.txt
	
RUN pip install -r requirements.txt

COPY . /app



