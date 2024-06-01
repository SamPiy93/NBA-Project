from rest_framework import serializers

from NBA_API.models import GamePlayer


class GamePlayerSerializer(serializers.ModelSerializer):
    """
        serializer for Game Player model
    """

    class Meta:
        model = GamePlayer
        fields = '__all__'
