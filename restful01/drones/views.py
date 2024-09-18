from drones.models import Drone, DroneCategory, Pilot, Competition
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
# ModelViewSet inclui operações de CRUD
# class DroneCategoryViewSet(viewsets.ModelViewSet):
#     queryset = DroneCategory.objects.all()
#     serializer_class = DroneCategorySerializer
#     name = "dronecategory-viewset"


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = "dronecategory-list"


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = "dronecategory-detail"


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-list"


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-detail"


class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-list"


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-detail"


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-list"


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-detail"


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "drone-categories": reverse(DroneCategoryList.name, request=request),
                "drones": reverse(DroneList.name, request=request),
                "pilots": reverse(PilotList.name, request=request),
                "competitions": reverse(CompetitionList.name, request=request),
            }
        )
