from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status, permissions, generics
from .serializers import *
from rest_framework.generics import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from taggit.models import Tag
from django.http import JsonResponse
from textblob import TextBlob
from django.contrib.auth.decorators import login_required
import readtime


class BlogView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializers

    def get_queryset(self):
        user_instance=User.objects.get(username=self.request.user)
        return Blog.objects.filter(user=user_instance)

class Allupdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

    def perform_update(self, serializer):
        user_instance = User.objects.get(username=self.request.user)
        serializer.save(user=user_instance)
        return Response(serializer.data, status=200)

    lookup_field = "id"
    

class BlogCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogCreateSerializers

    def perform_create(self, serializer):
        user_instance = User.objects.get(username=self.request.user)
        post_data = self.request.data
        
        result = readtime.of_text(post_data['body'], wpm=275)
        r=result.seconds
        hour, minutes, seconds= 0,0,0
        seconds = r % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        new_timetoread=Timetoread.objects.create(hours=hour, mins=minutes, secs=seconds )
        new_timetoread.save()
        
        new_blog=Blog.objects.create(
            user=user_instance, title=post_data["title"], description=post_data["description"], body=post_data["body"], published=False, timetoreads=new_timetoread
        )
        if post_data["tags"] is not None:
            for i in post_data["tags"]:
                new_blog.tags.add(i)
        new_blog.save()

        serializer=BlogCreateSerializers(new_blog)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BlogUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializers
    
    def get_queryset(self):
        _id=self.kwargs['id']
        obj=Blog.objects.get(id=_id)
        obj.published=True
        obj.save()
        user_instance=User.objects.get(username=self.request.user)
        return Blog.objects.filter(user=user_instance, id=_id)
    
    def perform_update(self, serializer):
        post_data = self.request.data
        _id=self.kwargs['id']
        result = readtime.of_text(post_data['body'], wpm=275)
        r=result.seconds
        hour, minutes, seconds= 0,0,0
        seconds = r % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        
        time_read=Timetoread.objects.get(id=post_data['id'])
        time_read.hours=hour
        time_read.mins=minutes
        time_read.secs=seconds
        time_read.save()
        

        user_instance = User.objects.get(username=self.request.user)
        serializer.save(user=user_instance)
        return Response(serializer.data, status=200)

    lookup_field = "id"
    


class BlogPublishView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializers

    def get_queryset(self):
        publish=self.kwargs['publish']
        # user_instance = User.objects.get(username=self.request.user)
        return Blog.objects.filter(published=publish)


class SpellCheckView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request, *args, **kwargs):
        
        _id = self.kwargs['_id']
        obj = Blog.objects.get(id=_id)
        li = list(obj.body.split(" "))
        miss=[]
        length=len(li)
        for i in range(length):
            if(li[i] != TextBlob(li[i]).correct()):
                miss.append(li[i])
        response_data = {"misspelledWords": miss}
        return JsonResponse(response_data, status=200)

