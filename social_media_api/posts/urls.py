from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
     path('api/', include('accounts.urls')),  # Add the accounts URLs here
    path('api/', include('posts.urls')),    # Add the posts URLs here
]