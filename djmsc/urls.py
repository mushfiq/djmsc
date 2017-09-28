from django.conf.urls import url, include

from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r"event", views.EventViewSet)
router.register(r"person", views.PersonViewSet)


urlspattern = router.urls

