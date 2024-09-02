# from rest_framework import status
# from drones.models import Drone, Competition, Pilot, DroneCategory
# from drones.serializers import (
#     DroneSerializer,
#     DroneCategorySerializer,
#     CompetitionSerializer,
#     PilotCompetitionSerializer,
#     PilotSerializer,
# )
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(["GET", "POST"])
# def droneCategory_list(request):
#     if request.method == "GET":
#         droneCategory = DroneCategory.objects.all()
#         dronesCategory_serializer = DroneCategorySerializer(droneCategory, many=True)
#         return Response(dronesCategory_serializer.data)

#     elif request.method == "POST":
#         dronesCategory_serializer = DroneCategorySerializer(data=request.data)
#         if dronesCategory_serializer.is_valid():
#             dronesCategory_serializer.save()
#             return Response(
#                 dronesCategory_serializer.data, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             dronesCategory_serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )


from asyncio import mixins
from django.shortcuts import render
from rest_framework import generics
from drones.models import DroneCategory
from drones.models import Drone
from drones.serializers import DroneCategorySerializer
from drones.serializers import DroneSerializer
from drones.models import Pilot
from drones.models import Competition
from drones.serializers import PilotSerializer
from drones.serializers import PilotCompetitionSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
# from rest_framework.decorators import api_view, GenericAPIView


class DroneCategoryViewSet(viewsets.ModelViewSet):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = "dronecategory-viewset"


# class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = DroneCategory.objects.all()
#     serializer_class = DroneCategorySerializer
#     name = "dronecategory-detail"


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = "dronecategory-list"


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
                "drone-categories": reverse(DroneCategoryViewSet.name, request=request),
                "drones": reverse(DroneList.name, request=request),
                "pilots": reverse(PilotList.name, request=request),
                "competitions": reverse(CompetitionList.name, request=request),
            }
        )
