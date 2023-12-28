from django.urls import path
from . import views

urlpatterns=[
    path('',views.trip),
    # path('hotelacc/',views.hotel),
    # path('index/',views.login),
    # path('team/',views.team),
]