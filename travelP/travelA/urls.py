from django.urls import path
from . import views

urlpatterns=[
    path('',views.payment),
    # path('hotelacc/',views.hotel),
    # path('index/',views.login),
    # path('team/',views.team),
]