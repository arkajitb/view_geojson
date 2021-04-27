### Run docker-compose

- To start the server in your localhost, run:
```console
$ docker-compose up
```

You can test all the functionalities in postman
### api functionalities

#### api-root
```console
http://0.0.0.0:8000/api
```
#### Create JSON Web Token (method=['POST'])
`http://0.0.0.0:8000/api/token/`

In the body, add uthe following key-value pairs
| key      | value |
|----------|-------|
| username | admin |
| password | admin |

Note: provide these values under body -> x-www-form-urlencoded

If you want to create a new superuser, run the command below in your console:
```console
$ docker-compose run web python manage.py createsuperuser
```
the request will generate two key-value pairs:
refresh: {}
access: {}
Use the access token to access all the api routes mentioned below.
If the access token expires, go to `http://0.0.0.0:800/api/token/refresh`, provide refresh as key and the copied refresh value as 
value under body->x-www-form-urlencoded.
You will get the new access token.

#### Upload all the features from municipalities_nl.geojson(method=['POST'])
`http://0.0.0.0:8000/api/locations/upload_data/`

#### View all the feature objects(100 features per page)(method=['GET'])

`http://0.0.0.0:8000/api/locations/`

#### Filter features based on bounding box (method=[GET])

`http://0.0.0.0:8000/api/locations/?in_bbox=[]`

#### Filter features based on municipality name (method=[GET])

`http://0.0.0.0/api/locations/{name}`

#### Add a new location

`http://0.0.0.0:8000/api/location?name={name}&` (method=[POST])

