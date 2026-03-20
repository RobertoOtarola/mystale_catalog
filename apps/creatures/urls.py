from django.urls import path
from .views import CreatureListView, CreatureDetailView, CreatureCreateView

app_name = 'creatures'

urlpatterns = [
    path('',              CreatureListView.as_view(),  name='list'),
    path('<int:pk>/',     CreatureDetailView.as_view(), name='detail'),
    path('new/',          CreatureCreateView.as_view(), name='create'),
]
