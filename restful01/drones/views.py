from drones.models import (Drone, DroneCategory, Pilot, Competition, Person)
from drones.serializers import (
    DroneSerializer,
    DroneCategorySerializer,
    PilotSerializer,
    PilotCompetitionSerializer,
    PersonSerializer
)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, viewsets
from django_filters import rest_framework as filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
from drones.filters import CompetitionFilter

# Aqui implementamos uma classe Viewsets - Combina a logica de um conjunto de views relacionadas em uma única classe.
# É Uma class-based view que não fornece métodos get ou post, porém ações list() e create()
# ModelViewSet inclui operações de CRUD, é a solução para tudo em uma só classe
class DroneCategoryViewSet(viewsets.ModelViewSet):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = "dronecategory-list"
    search_fields = ("^name",) # Busca <------------------------
    ordering_fields = ("name",) # Ordenação <------------------------
class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-list"
    filterset_fields = (  # Filtro <------------------------
        "drone_category",
        "has_it_competed",
    )
    search_fields = ("^name",)
    ordering_fields = (
        "name",
        "manufacturing_date",
    )

class PilotViewSet(viewsets.ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-list"
    filterset_fields = (
        "gender",
        "races_count",
    )
    search_fields = ("^name",)
    ordering_fields = ("name", "races_count")

class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-list"
    # filterset_class = CompetitionFilter
    ordering_fields = (
        "distance_in_feet",
        "distance_achievement_date",
    )


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    name = "person-list"
    search_fields = ("^name",)
    ordering_fields = ("name",)


class ApiRoot(generics.GenericAPIView):
    name = "api-root"
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "drone-categories": reverse("dronecategory-list", request=request),
                "drone": reverse("drone-list", request=request),
                "pilots": reverse("pilot-list", request=request),
                "competitions": reverse("competition-list", request=request),
                "person": reverse("person-list", request=request)
            }
        )
