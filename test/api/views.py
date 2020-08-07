from django.shortcuts import render
from .models import Device
from .serializers import DeviceSerializer
from rest_framework import viewsets,permissions,status
from rest_framework.response import Response
from django.db.models import  Max
from rest_framework import generics


# Create your views here.

class DeviceList(generics.RetrieveAPIView):
    serializer_class = DeviceSerializer
    permission_classes=(permissions.AllowAny,)

    def get_object(self):
        query_set = Device.objects.filter(platform=self.request.query_params.get("platform", None)).order_by('-version').first()

        return query_set



class StoreDeviceList(generics.CreateAPIView):
    serializer_class = DeviceSerializer
    permission_classes=(permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        if Device.objects.filter(version=request.data.get("version")):
            return Response({"error": "Version already exists!",
                             "status": status.HTTP_400_BAD_REQUEST,
                             "url": request.path},
                            status=status.HTTP_400_BAD_REQUEST)

        pay_load = Device.objects.create(
            platform=request.data.get("platform"),
            version=request.data.get("version"),
        )

        return Response({"msg": "Your data has been added successfully!",
                         "status": status.HTTP_200_OK,
                         "payload": self.get_serializer(pay_load).data,
                         "url": request.path}, status.HTTP_200_OK)