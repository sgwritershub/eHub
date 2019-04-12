from django.urls import path
from . import views
from.views import HomeListView, HomeDetailView, HomeCreateView, HomeUpdateView, HomeDeleteView

urlpatterns = [
    path('', HomeListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', HomeDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', HomeUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', HomeDeleteView.as_view(), name='post-delete'),
    path('post/new', HomeCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about')
]
