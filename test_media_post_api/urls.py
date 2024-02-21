from django.contrib import admin
from django.urls import path, include
from test_media_post_api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/media-post', include(api_urls)),
]