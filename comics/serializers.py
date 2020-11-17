from rest_framework import serializers
from master.models import UserComics, Comic


class UserComicSerializer(serializers.ModelSerializer):
    comic_id = serializers.SerializerMethodField(source='id')
    release_date = serializers.SerializerMethodField(source='dates')
    class Meta:
        model = Comic
        # fields = '__all__'
        exclude = ('id', )
        depth = 2
        
    def get_user_comics(self, user):
        return UserComics.objects.get_or_create(user=user)

    def save(self, user):
        comic = super(UserComicSerializer, self).save()
        user_comic = self.get_user_comics()
        user_comic.add(comic)
        return comic
        
    