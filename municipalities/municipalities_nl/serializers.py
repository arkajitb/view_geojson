from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Location


# Create a serializer for Location model.
class LocationSerializer(GeoFeatureModelSerializer): 
	class Meta:
		model = Location
		geo_field = 'geometry'
		fields = '__all__'

		
