"""
    route configuration of NBA API
"""

from django.urls import path, include
from NBA_API import views
from rest_framework import routers

"""
    register login routes with automatic routing
"""
router = routers.DefaultRouter()
router.register("users", views.UserListView)
router.register("groups", views.UserGroupListView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('players/', views.PlayerListCreateView.as_view(), name='player-list-create'),
    path('players/<int:pk>', views.PlayerListUpdateDeleteView.as_view(), name='player-list-update-delete'),
    path('teams/', views.TeamListCreateView.as_view(), name='team-list-create'),
    path('teams/<int:pk>', views.TeamListUpdateDeleteView.as_view(), name='team-list-update-delete'),
    path('games/', views.GameListCreateView.as_view(), name='game-list-create'),
    path('games/<int:pk>', views.GameListUpdateDeleteView.as_view(), name='game-list-update-delete'),
    path('player-scores/', views.GamePlayerListCreateView.as_view(), name='game-player-list-create'),
    path('player-scores/', views.GamePlayerListUpdateDeleteView.as_view(), name='game-player-list-update-delete'),
    path('teams/top-players/<int:id>', views.TopPlayersView, name='top-player-list')
]
