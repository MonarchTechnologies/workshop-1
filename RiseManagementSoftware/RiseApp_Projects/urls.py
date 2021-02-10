from django.urls import path, include
from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/projects', api.ProjectView)
router.register('api/tasks', api.TaskView)

urlpatterns = router.urls