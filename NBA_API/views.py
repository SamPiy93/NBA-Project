import numpy as np
from django.contrib.auth.models import Group, User
from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication

from NBA_API.models import Player, Team, Game, GamePlayer
from NBA_API.permissions.custom_permissions import CoachPermission, AdminPermission, PlayerPermission
from NBA_API.serializers.GamePlayerSerializer import GamePlayerSerializer
from NBA_API.serializers.GameSerializer import GameSerializer
from NBA_API.serializers.GroupSerializer import GroupSerializer
from NBA_API.serializers.PlayerSerializer import PlayerSerializer
from NBA_API.serializers.TeamSerializer import TeamSerializer
from NBA_API.serializers.UserSerializer import UserSerializer


class UserListView(viewsets.ModelViewSet):
    """
        retrieval endpoint for Users
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission | CoachPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGroupListView(viewsets.ModelViewSet):
    """
        retrieval endpoint for Groups
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission | CoachPermission]

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PlayerListCreateView(generics.ListCreateAPIView):
    """
        retrieval & creation endpoint for Players
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission]

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        retrieval, update & delete endpoint for Players
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission | CoachPermission | PlayerPermission]

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TeamListCreateView(generics.ListCreateAPIView):
    """
        retrieval & create endpoint for Teams
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission | CoachPermission]

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        retrieval, update & delete endpoint for Teams
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission | CoachPermission]

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class GameListCreateView(generics.ListCreateAPIView):
    """
        retrieval & create endpoint for Games
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission | CoachPermission]

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        retrieval, update & delete endpoint for Games
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission | CoachPermission]

    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission]

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GamePlayerListCreateView(generics.ListCreateAPIView):
    """
        retrieval & create endpoint for Game-Players
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission | CoachPermission | PlayerPermission]

    queryset = GamePlayer.objects.all()
    serializer_class = GamePlayerSerializer


class GamePlayerListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        retrieval, update & delete endpoint for Game-Players
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission | CoachPermission]

    queryset = GamePlayer.objects.all()
    serializer_class = GamePlayerSerializer


class TopPlayersView(generics.ListAPIView):
    """
        endpoint to find the Top Players of a particular team when team id provided
    """

    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminPermission | CoachPermission]
    serializer_class = PlayerSerializer

    def get_queryset(self):
        # fetch team by id
        id = self.kwargs.get('id')
        team = Team.objects.get(id=id)
        team_players = Player.objects.filter(team=team)
        sorted_team_players_by_average_score = sorted(team_players, key=lambda player: player.average_score)
        sorted_average_scores = list(map(lambda player: player.average_score, sorted_team_players_by_average_score))
        # fetch ninetieth percentile score from numpy
        ninetieth_percentile_score = np.percentile(sorted_average_scores, 90)
        # filter and list players who's average score is over ninetieth percentile score of the team
        return list(filter(lambda player: player.average_score >= ninetieth_percentile_score, team_players))
