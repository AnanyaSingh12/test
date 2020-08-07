from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    
    url('admin/', admin.site.urls),
    url(r'^apiauth/', include('rest_auth.urls')),
    url(r'^api/', include('api.urls')),
    
    
]
