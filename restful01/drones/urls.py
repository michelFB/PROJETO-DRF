from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter

# Cria uma pagina especifica que mostra todas as rotas
router = SimpleRouter()
router.register(r"drone-categories", views.DroneCategoryViewSet) #Inclui a ViewSET
router.register(r"drones", views.DroneViewSet)
router.register(r"pilots", views.PilotViewSet)
router.register(r"competitions", views.CompetitionViewSet)
router.register(r"person", views.PersonViewSet)

urlpatterns = [ 
    #   path(
    #     "drones/",
    #     views.DroneList.as_view(),
    #     name=views.DroneList.name,
    # ),
    # path(
    #     "drones/<int:pk>/",
    #     views.DroneDetail.as_view(),
    #     name=views.DroneDetail.name,
    # ),
    path("", include(router.urls)),
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),
]

urlpatterns += router.urls
