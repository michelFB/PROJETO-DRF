from drones.models import (Drone, DroneCategory, Pilot, Competition)
from drones.serializers import (
    DroneSerializer,
    DroneCategorySerializer,
    PilotSerializer,
    PilotCompetitionSerializer,
)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, viewsets


# Aqui implementamos uma classe Viewsets - Combina a logica de um conjunto de views relacionadas em uma única classe.
# É Uma class-based view que não fornece métodos get ou post, porém ações list() e create()
# ModelViewSet inclui operações de CRUD, é a solução para tudo em uma só classe
class DroneCategoryViewSet(viewsets.ModelViewSet):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = "dronecategory-list"
class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-list"

class PilotViewSet(viewsets.ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-list"

class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-list"


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "drone-categories": reverse("dronecategory-list", request=request),
                "drone": reverse("drone-list", request=request),
                "pilots": reverse("pilot-list", request=request),
                "competitions": reverse("competition-list", request=request)
            }
        )
