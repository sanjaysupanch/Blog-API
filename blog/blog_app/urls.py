from django.urls import path,include
from .views import *
from blog_app import views


urlpatterns = [
    
    path('api/', include('rest_auth.urls')),
    path('api/registration/', include('rest_auth.registration.urls')),
    path('api/story/', BlogView.as_view()),
    path('api/post/', BlogCreateView.as_view()),
    path('api/story/<id>/publish/', BlogUpdate.as_view()),
    path('api/story/<id>/', Allupdate.as_view()),
    path('api/publish/<publish>/', BlogPublishView.as_view()),
    path('api/spellcheck/<int:_id>/', SpellCheckView.as_view(   )),
]
