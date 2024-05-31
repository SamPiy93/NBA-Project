from rest_framework import generics

from NBA_API.models import User
from NBA_API.serializers.UserSerializer import UserSerializer


# Create your views here.
class UserCreationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AllUsersRetrievalAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrievalAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

