from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'', views.default_map, name="default"),
]