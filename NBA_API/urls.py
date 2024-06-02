from django.urls import path, include
from NBA_API import views
from rest_framework import routers

"""
    register API routes and auth routes
"""
router = routers.DefaultRouter()
router.register("api/users", views.UserListView)
router.register("api/groups", views.UserGroupListView)

urlpatterns = [
    path('', include(router.urls)),
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
