from rest_framework import serializers, status
from django.contrib.auth.models import User
from .models import *
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)


class timetoreadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Timetoread
        fields=['id','hours','mins','secs']


class BlogCreateSerializers(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Blog
        fields = ['id', 'tags', 'title', 'description', 'body' ]



class BlogSerializers(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    timetoreads = timetoreadSerializer()
    class Meta: 
        model = Blog
        fields = ['id','tags', 'title', 'description',
                  'body','published', 'timetoreads', ]
        
        depth=1
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.published = validated_data.get('published', instance.published)
        instance.save()

        ttreads_data=validated_data.pop('timetoreads')
        ttread1=instance.timetoreads
        ttread1.hours=ttreads_data.get('hours',ttread1.hours)
        ttread1.mins = ttreads_data.get('mins', ttread1.mins)
        ttread1.secs = ttreads_data.get('secs', ttread1.secs)
        ttread1.save()
        return instance

