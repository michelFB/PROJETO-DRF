from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter() #Cria uma pagina especifica que mostra todas as rotas
router.register(r"drone-categories", views.DroneCategoryViewSet) #Inclui a ViewSET

urlpatterns = [
    path(
        "drone-categories/",
        views.DroneCategoryList.as_view(),
        name=views.DroneCategoryList.name,
    ),
    path(
        "drone-categories/<int:pk>/",
        views.DroneCategoryDetail.as_view(),
        name=views.DroneCategoryDetail.name,
    ),
    path(
        "drones/",
        views.DroneList.as_view(),
        name=views.DroneList.name,
    ),
    path(
        "drones/<int:pk>/",
        views.DroneDetail.as_view(),
        name=views.DroneDetail.name,
    ),
    path(
        "pilots/",
        views.PilotList.as_view(),
        name=views.PilotList.name,
    ),
    path(
        "pilots/<int:pk>/",
        views.PilotDetail.as_view(),
        name=views.PilotDetail.name,
    ),
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
    path("", include(router.urls)),
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),
]

urlpatterns += router.urls
