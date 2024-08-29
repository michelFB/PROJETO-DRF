from django.urls import path
from . import views

urlpatterns = [
    path("drones/", views.droneCategory_list),
#     path("drones/<int:pk>", views.toy_detail),
]
