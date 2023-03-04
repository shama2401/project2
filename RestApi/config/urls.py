from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/base-auth/', include('rest-framework.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/v1/base-auth/', include('store.urls')),

]
