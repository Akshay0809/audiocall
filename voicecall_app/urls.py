'''from django.urls import path
from .views import *

urlpatterns = [
    path("app/", main_view,name="mainview" ),
]'''


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('call/<str:pin_code>/', views.call, name='call'),
]

