## Backend Coding Assignment

Create a small Django REST API using Django REST Framework serving vector features in a GeoJSON compatible format.

The main goal of this assignment is to assess how you structure your code and workflow
and to give you a head start on the kind of data we process.

The Django server should offer the following:
- A CRUD REST API for GeoJSON feature objects. A real FeatureCollection object
does not allow for paging (limiting the amount of features returned), so a result page
may look like this:

```yaml
{
"next": "http://example.com/features/?page=3"
"prev": "http://example.com/features/?page=1"
"results": [<GeoJSON Feature Object>, ...]
}
```

**Hint**: use the djangorestframework package

- The features should be able to be filtered by a boundingbox (e.g. you are only viewing part of the map) and the results should be paged (100 features per request).
**Hint**: use the djangorestframework-gis package for bounding box filters.

- Use the provided dataset (municipalities in the Netherlands) and write a python script to read the file and post to the API.
Hint: use the geopandas package, a geospatial extension of the pandas framework.

Optional

- Bonus points: provide a Dockerfile and docker-compose.yml to build and test your
application easily into a docker container with supporting services (a postgis
database e.g.)

- Bonus points: The API should use json web tokens for authorization.

## Deliverables

- A link to a public git repository.
- A zip archive containing the following:
	- All your source code and other assets required to run and build the app.
	- A short README.md with instructions on how to run and build the app.