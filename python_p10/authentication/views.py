from rest_framework import viewsets, permissions

from python_p10.authentication.models import User
from python_p10.authentication.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_time')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
