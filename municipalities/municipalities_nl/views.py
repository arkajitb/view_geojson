# External imports
from rest_framework import viewsets
from .serializers import LocationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_gis.filters import InBBoxFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.gis.geos import GEOSGeometry
import geopandas as gpd
from pathlib import Path
from os import path

# Internal imports
from .models import Location

# View for Location model.
class LocationView(viewsets.ModelViewSet):

	serializer_class = LocationSerializer
	pagination_class = PageNumberPagination
	bbox_filter_field = 'geometry'
	filter_backends = (InBBoxFilter,)
	bbox_filter_include_overlapping = True
	permission_classes = [IsAuthenticated]

	# Get 100 objects per page.
	def get_queryset(self):
		locations = Location.objects.all()
		return locations

	# Retreive features for a particular location based on the name.
	def retrieve(self, request, *args, **kwargs):
		params = kwargs
		location = Location.objects.filter(name = params['pk'])
		serializer = LocationSerializer(location, many=True)
		if serializer.data['features']:
			return Response(serializer.data)
		else:
			return Response({'Features not available for the current location provided.'})

	# Create feature objects from a file path provided.
	@action(detail=False, methods = ['post'])
	def upload_data(self, request):
		file_path = Path('municipalities_nl.geojson')
		gdf = gpd.read_file(file_path)

		# Iterate through each geoJSON object and create an object for Location model.
		for data in gdf.to_dict('records'):
			name = data["name"]
			try:
				geometry = GEOSGeometry(str(data["geometry"]))
			except(TypeError, ValueError) as exec:
				# If geometry is not valid or none continue with the next feature.
				continue
			if geometry.geom_type != 'MultiPolygon':
				# If the created geometry is not a Multipolygon, continue with the next feature.
				continue
			Location.objects.update_or_create(
				name = name,
				geometry = GEOSGeometry(geometry),
				)
		return Response({'Data uploaded from the file successfully'})

	



	

		
			










