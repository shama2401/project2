from rest_framework import routers
from .views import BookViewSet




routers = routers.SimpleRouter()


routers.register(r'book', BookViewSet)


urlpatterns = []
urlpatterns += routers.urls
