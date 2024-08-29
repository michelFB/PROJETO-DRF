# from django.shortcuts import render
from rest_framework import status
from drones.models import Drone, Competition, Pilot, DroneCategory
from drones.serializers import DroneSerializer, DroneCategorySerializer, CompetitionSerializer, PilotCompetitionSerializer, PilotSerializer
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
            return Response(dronesCategory_serializer.data, status=status.HTTP_201_CREATED)
        return Response(dronesCategory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def toy_detail(request, pk):
#     try:
#         toy = Toy.objects.get(pk=pk)
#     except Toy.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         toy_serializer = droneserializer(toy)
#         return Response(toy_serializer.data)

#     elif request.method == "PUT":
#         toy_serializer = droneserializer(toy, data=request.data)
#         if toy_serializer.is_valid():
#             toy_serializer.save()
#             return Response(toy_serializer.data)
#         return Response(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         toy.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


