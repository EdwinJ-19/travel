from django.urls import path
from . import views

urlpatterns=[
    path('',views.hotel),
    # path('hotelacc/',views.hotel),
    # path('index/',views.login)
]