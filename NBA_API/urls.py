from django.urls import path, include
from rest_framework.response import Response
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.views import APIView

from NBA_API import views
from rest_framework import routers

"""
    register API routes and auth routes
"""
router = routers.DefaultRouter()
router.register(r"api/users", views.UserListView)
router.register(r"api/groups", views.UserGroupListView)


class CustomAPIRoot(APIView):
    def get(self, request, format=None):
        data = {
            'users': reverse('user-list', request=request, format=format),
            'groups': reverse('group-list', request=request, format=format),
            'players list/create': reverse('player-list-create', request=request, format=format),
            'teams list/create': reverse('team-list-create', request=request, format=format),
            'games list/create': reverse('game-list-create', request=request, format=format),
            'game-player  list/create': reverse('game-player-list-create', request=request, format=format),
        }
        return Response(data)


urlpatterns = [
    path('', CustomAPIRoot.as_view(), name='custom-api-root'),
    path('', include(router.urls), name='api-root'),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/players/', views.PlayerListCreateView.as_view(), name='player-list-create'),
    path('api/players/<int:pk>', views.PlayerListUpdateDeleteView.as_view(), name='player-list-update-delete'),
    path('api/teams/', views.TeamListCreateView.as_view(), name='team-list-create'),
    path('api/teams/<int:pk>', views.TeamListUpdateDeleteView.as_view(), name='team-list-update-delete'),
    path('api/games/', views.GameListCreateView.as_view(), name='game-list-create'),
    path('api/games/<int:pk>', views.GameListUpdateDeleteView.as_view(), name='game-list-update-delete'),
    path('api/player-scores/', views.GamePlayerListCreateView.as_view(), name='game-player-list-create'),
    path('api/player-scores/', views.GamePlayerListUpdateDeleteView.as_view(), name='game-player-list-update-delete'),
    path('api/teams/top-players/<int:id>', views.TopPlayersView.as_view(), name='top-player-list')
]
