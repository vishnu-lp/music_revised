from rest_framework.serializers import ModelSerializer


from .models import Music

class MusicSerializer(ModelSerializer):
	class Meta:
		model = Music
		fields = ['id','music_title','music_description','music_genre']