import os
from math import floor

from django.contrib.auth.models import User
from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase


class NBAProjectTest(APITestCase):

    def setUp(self):
        '''
        load test data using fixtures
        '''
        FIXTURES_DIR = 'NBA_API/fixtures'
        fixtures = [[
            os.path.join(FIXTURES_DIR, file_name)
            for file_name in os.listdir(FIXTURES_DIR)
            if file_name.endswith('.json')
        ]]
        # load test data from fixtures
        call_command('loaddata', *fixtures)

    def test_games_endpoint_with_authorized_coach(self):
        """
            successfully authorize Games endpoint with user(Coach)
        """
        self._auth_user(11)

        response = self.client.get('/api/games/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_games_endpoint_with_unauthorized_player(self):
        """
            return forbidden upon authorize Games endpoint with user(Player)
        """
        self._auth_user(101)

        response = self.client.get('/api/games/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_retrieval(self):
        """
            successfully retrieve all Users
        """
        self._auth_user(1)

        response = self.client.get('/api/users/')
        self.assertTrue(response.status_code == status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_top_players_endpoint_for_team_1(self):
        """
            successfully fetch Top Players list per team upon providing the Team Id
        """
        self._auth_user(11)

        response = self.client.get('/api/teams/1')
        players = list(response.data['players'])
        average_scores = list(map(lambda player: player['average_score'], players))
        average_scores.sort()
        ninetieth_percentile_index = floor(len(average_scores) * 0.9)
        expected_ninetieth_percentile_score = average_scores[ninetieth_percentile_index]

        top_players = self.client.get('/api/teams/top-players/1').json()
        for player in top_players:
            self.assertTrue(expected_ninetieth_percentile_score <= player['average_score'])

    def test_top_players_endpoint_for_unauthorized_player(self):
        """
            successfully authorize Top Players endpoint with user(Player)
        """
        # access top players endpoint by a team player
        self._auth_user(101)

        response = self.client.get('/api/teams/1')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def _auth_user(self, pk):
        user = User.objects.get(pk=pk)
        self.client.force_authenticate(user=user)
