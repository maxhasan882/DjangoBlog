from django.urls import path
from . import views


urlpatterns = {
    path('', views.home),
    path('single', views.GetSinglePost),
    path('profile', views.getProfile)
}
