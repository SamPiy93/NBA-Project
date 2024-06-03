from rest_framework import serializers

from NBA_API.models import Team
from NBA_API.serializers.PlayerSerializer import PlayerSerializer


class TeamSerializer(serializers.ModelSerializer):
    """
        serializer for Team model
    """

    players = PlayerSerializer(many=True, read_only=True)
    average_score = serializers.SerializerMethodField()

    def get_average_score(self, obj):
        return obj.average_score

    class Meta:
        model = Team
        fields = '__all__'
