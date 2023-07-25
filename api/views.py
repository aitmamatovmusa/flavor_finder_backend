from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Place, Comment
from .serializers import PlaceSerializer, CommentSerializer


class PlaceList(APIView):
    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response({"places": serializer.data})

    def post(self, request):
        place_fields = {
            **request.data,
            "num_reviews": 0,
            "rating": 0.0,
        }

        serializer = PlaceSerializer(data=place_fields)

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


class CommentList(APIView):
    def get(self, request):
        place_pk = request.query_params.get("place")
        comments = (
            Comment.objects.filter(place_id=place_pk)
            if place_pk
            else Comment.objects.all()
        )
        serializer = CommentSerializer(comments, many=True)
        return Response({"comments": serializer.data})

    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
