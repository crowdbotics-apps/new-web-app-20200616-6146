from rest_framework import authentication
from users.models import TestModel
from .serializers import TestModelSerializer
from rest_framework import viewsets


class TestModelViewSet(viewsets.ModelViewSet):
    serializer_class = TestModelSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TestModel.objects.all()
