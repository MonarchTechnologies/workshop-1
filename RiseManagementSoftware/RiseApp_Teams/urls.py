from django.urls import include,path
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register('api/teams', api.TeamView)

urlpatterns = router.urls
