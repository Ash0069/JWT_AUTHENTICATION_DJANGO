from django.contrib import admin
from django.urls import path, include
from users import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(url))
]
