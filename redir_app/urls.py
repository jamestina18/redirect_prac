from django.urls import path
from . import views
urlpatterns = [
     # path('admin/', admin.sites.urls) 
    path('',views.index),
    path('add_user', views.add_user),
    path('show',views.show)
]