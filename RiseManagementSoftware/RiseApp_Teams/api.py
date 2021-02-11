from rest_framework import viewsets, permissions
from .models import Team
from .serializers import TeamSerializer
# Create your views here.

class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeamSerializer