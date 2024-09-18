from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path(
        "drone-categories/",
        views.droneCategory_list,
    ),
    # path("drones/", views.DroneList.as_view(), name=views.DroneList.name),
    # path("drones/<int:pk>/", views.DroneDetail.as_view(), name=views.DroneDetail.name),
]

