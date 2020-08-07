from django.conf.urls import url, include
from rest_framework import routers
from .views import *


app_name = 'api'
#



urlpatterns = [
    url('device/',DeviceList.as_view()),
    url('device-store/',StoreDeviceList.as_view())

]