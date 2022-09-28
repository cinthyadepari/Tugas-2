from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    path("list_task", views.show_todolist, name= 'list_task'),
    path('create_task', views.create_task, name= 'create_task'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # path('html', views.readHtml, name= 'readHtml'),
    # path('xml', views.readXml, name="readXml"),
    # path('json', views.readJson, name="readjson"),
]