from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Place
from .serializers import PlaceSerializer


class PlaceList(APIView):
    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response({"places": serializer.data})

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaceDetail(APIView):
    def get(self, request, pk):
        place = Place.objects.get(pk=pk)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

    def put(self, request, pk):
        place = Place.objects.get(pk=pk)
        serializer = PlaceSerializer(place, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        place = Place.objects.get(pk=pk)
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
