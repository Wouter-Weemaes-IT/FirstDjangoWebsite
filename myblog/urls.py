
from django.urls import path
from . import views
from .views import HomeView, ArticDetailView, AddPostView, UpdatePostView
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>',ArticDetailView.as_view(), name="artic-details" ),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post')
]
