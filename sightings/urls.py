from  django.urls import path
from . import views
app_name = 'sightings'
urlpatterns = [
        path('add', views.add, name='add'),
        path('stats', views.stats, name='stats'),
        path('', views.sightings, name='sightings'),
        path('<str:unique_squirrel_id>', views.update, name='update'),
        path('<str:unique_squirrel_id>/delete', views.delete, name='delete'),
        ]
