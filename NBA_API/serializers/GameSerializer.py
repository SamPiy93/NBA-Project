from rest_framework import serializers

from NBA_API.models import Game, Team
from NBA_API.serializers.TeamSerializer import TeamSerializer


class GameSerializer(serializers.ModelSerializer):
    """
        serializer for Game model
    """

    team_won = serializers.SerializerMethodField()

    def get_team_won(self, obj):
        return obj.team_won

    class Meta:
        model = Game
        fields = '__all__'
