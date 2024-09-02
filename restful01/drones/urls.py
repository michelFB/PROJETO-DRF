from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"drone-categories", views.DroneCategoryViewSet)

urlpatterns = [
    path(
        "drone-categories/",
        views.DroneCategoryList.as_view(),
        name=views.DroneCategoryList.name,
    ),
    path("drones/", views.DroneList.as_view(), name=views.DroneList.name),
    path("drones/<int:pk>/", views.DroneDetail.as_view(), name=views.DroneDetail.name),
    path("pilots/", views.PilotList.as_view(), name=views.PilotList.name),
    path("pilots/<int:pk>/", views.PilotDetail.as_view(), name=views.PilotDetail.name),
    path(
        "competitions/",
        views.CompetitionList.as_view(),
        name=views.CompetitionList.name,
    ),
    path(
        "competitions/<int:pk>/",
        views.CompetitionDetail.as_view(),
        name=views.CompetitionDetail.name,
    ),
]

urlpatterns += router.urls
