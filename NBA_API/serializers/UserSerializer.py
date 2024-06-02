from rest_framework import serializers

from NBA_API.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
        serializer for User model(admin, coach, player)
    """

    class Meta:
        model = User
        fields = ["username", "email", "groups", "url"]
