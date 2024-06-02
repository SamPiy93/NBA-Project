from rest_framework import serializers

from NBA_API.models import Player
from NBA_API.serializers.GamePlayerSerializer import GamePlayerSerializer


class PlayerSerializer(serializers.ModelSerializer):
    """
        serializer for Player model
    """

    scores = GamePlayerSerializer(many=True, read_only=True)
    average_score = serializers.SerializerMethodField()

    def get_average_score(self, obj):
        return obj.average_score

    class Meta:
        model = Player
        fields = '__all__'
