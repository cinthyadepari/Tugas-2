from django.urls import path
from . import views

app_name = 'mywatchlist'

urlpatterns = [
    path('html', views.readHtml, name= 'readHtml'),
    path('xml', views.readXml, name="readXml"),
    path('json', views.readJson, name="readjson"),
]