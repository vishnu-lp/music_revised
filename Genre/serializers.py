from rest_framework.serializers import ModelSerializer


from .models import Genre

class GenreSerializer(ModelSerializer):
	class Meta:
		model = Genre
		fields = ['id','genre_title','desc']