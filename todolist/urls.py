from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    path("", views.show_todolist, name= 'show_todolist'),
    path('create_task', views.create_task, name= 'create_task'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    # path('html', views.readHtml, name= 'readHtml'),
    # path('xml', views.readXml, name="readXml"),
    path('json/', views.show_json, name="show_json"),
    path('/create_data', views.create_task_ajax, name='create_task_ajax'),
]