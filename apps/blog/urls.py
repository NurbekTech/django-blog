from django.urls import path
from apps.blog import views

urlpatterns = [path("", views.home_page, name="home")]
