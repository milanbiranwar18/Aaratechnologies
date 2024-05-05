from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.utils import verify_token
from .models import Shop, Review
from .serializers import ShopSerializer, ReviewSerializer


class ShopList(APIView):
    """
    Retrieve shops based on location sent via POST or create a new shop.
    """
    def post(self, request, format=None):
        if 'latitude' in request.data and 'longitude' in request.data:
            latitude = float(request.data['latitude'])
            longitude = float(request.data['longitude'])
            shops = Shop.objects.filter(
                location__latitude__range=(latitude - 0.1, latitude + 0.1),
                location__longitude__range=(longitude - 0.1, longitude + 0.1)
            )
            serializer = ShopSerializer(shops, many=True)
            return Response(serializer.data)
        elif 'name' in request.data:
            serializer = ShopSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Latitude and longitude are required parameters for getting nearby shops."}, status=status.HTTP_400_BAD_REQUEST)


class ShopDetail(APIView):
    """
    Retrieve a shop by id, or post a review to a shop.
    """
    def get(self, request, pk, format=None):
        try:
            shop = Shop.objects.get(pk=pk)
            serializer = ShopSerializer(shop)
            return Response(serializer.data)
        except Shop.DoesNotExist:
            return Response({"error": "Shop not found"}, status=status.HTTP_404_NOT_FOUND)

    @verify_token
    def post(self, request, pk, format=None):
        try:
            shop = Shop.objects.get(pk=pk)
            review_data = request.data
            review_data['shop'] = shop.id
            review_data['user'] = request.user.id
            serializer = ReviewSerializer(data=review_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Shop.DoesNotExist:
            return Response({"error": "Shop not found"}, status=status.HTTP_404_NOT_FOUND)
