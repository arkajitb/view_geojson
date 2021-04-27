### Run docker-compose
Change directory to `municipalities`
- To start the server in your localhost, run:
```console
$ docker-compose up
```

You can test all the functionalities in postman or using curl.
The data is best viewed using postman.
Creation of web token and authentication examples are given in curl to give a basic understanding of how curl works.
### api functionalities

#### api-root

`http://0.0.0.0:8000/api`

If you want to create a new superuser, run the command below in your console:
```console
$ docker-compose run web python manage.py createsuperuser
```

#### Create JSON Web Token (method=['POST'])
`curl -X POST -H "Content-Type:application/json" -d '{"username": "admin", "password": "admin"}' http://0.0.0.0:8000/api/token/`

The request will return `access` and `refresh` tokens.

Use the access token to access all the api routes mentioned below.


#### Upload all the features from municipalities_nl.geojson
`curl -X POST -H "Accept: application/json" -H "Authorization: Bearer {Access_token}" http://0.0.0.0:8000/api/locations/upload_data/`


**Use postman for CRUD operations**
#### View all the feature objects(100 features per page)(method=['GET'])

`http://0.0.0.0:8000/api/locations/`

#### Filter features based on bounding box (method=[GET])

`http://0.0.0.0:8000/api/locations/?in_bbox=[]`

#### Filter features based on municipality name (method=[GET])

`http://0.0.0.0/api/locations/{id}`

#### Add a new location(method=[POST])

`http://0.0.0.0:8000/api/location/`

inside `body->x-www-form-urlencoded`
,pass `name` and `geometry` as the required keys and provide values for the same.

Note: `name` should not be present in the database already.

#### Update a location(method=[PATCH,PUT])
pass id of the object you want to update. In `body->x-www-form-urlencoded`, pass the field and the value you want to update.
`http://0.0.0.0:8000/api/location/{id}`

Note: PATCH is used to update a single field and PUT is used if you want to update all the fields.

#### Delete a location(method=[DELETE])

`http://0.0.0.0:8000/api/location/{id}`




	