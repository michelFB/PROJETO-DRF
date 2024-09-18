from rest_framework import status
from drones.models import Drone, Competition, Pilot, DroneCategory
from drones.serializers import (
    DroneSerializer,
    DroneCategorySerializer,
    CompetitionSerializer,
    PilotCompetitionSerializer,
    PilotSerializer,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def droneCategory_list(request):
    if request.method == "GET":
        droneCategory = DroneCategory.objects.all()
        dronesCategory_serializer = DroneCategorySerializer(droneCategory, many=True)
        return Response(dronesCategory_serializer.data)

    elif request.method == "POST":
        dronesCategory_serializer = DroneCategorySerializer(data=request.data)
        if dronesCategory_serializer.is_valid():
            dronesCategory_serializer.save()
            return Response(
                dronesCategory_serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            dronesCategory_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

