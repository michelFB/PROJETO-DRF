from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter

# router = DefaultRouter() #Cria uma pagina especifica que mostra todas as rotas
router = DefaultRouter()
router.register(r"drone-categories", views.DroneCategoryViewSet) #Inclui a ViewSET
router.register(r"drone", views.DroneViewSet)
router.register(r"pilots", views.PilotViewSet)
router.register(r"competitions", views.CompetitionViewSet)

urlpatterns = [
  
    path("", include(router.urls)),
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),
]

urlpatterns += router.urls
