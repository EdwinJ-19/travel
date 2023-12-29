from django.urls import path
from . import views

urlpatterns=[
    path('',views.team),
    # path('hotelacc/',views.hotel),
    # path('index/',views.login),
    # path('team/',views.team),
]