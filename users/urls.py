from django.urls import path,include
from .views import *
from . import views

app_name = "users"
urlpatterns = [
    path('<int:id>/follow_toggle/', follow_toggle, name="follow_toggle"),
 ]