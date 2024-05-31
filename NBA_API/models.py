from django.contrib.auth.models import User
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def average_score(self):
        total_score = 0
        total_games = 0

        for game in self.team1_games.all():
            total_score += game.team1_score
            total_games += 1
        for game in self.team2_games.all():
            total_score += game.team2_score
            total_games += 1

        if total_games > 0:
            return total_score / total_games

        return 0

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) #should check this
    name = models.CharField(max_length=100)
    height = models.PositiveIntegerField()
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE, null=True)

    @property
    def average_score(self):
        games = self.game_player.all()
        player_scores = [game.score for game in games]

        if not player_scores:
            return 0

        return sum(player_scores) / len(player_scores)

class Game(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_games', on_delete=models.CASCADE, null=True)
    team2 = models.ForeignKey(Team, related_name='team2_games', on_delete=models.CASCADE, null=True)
    team1_score = models.PositiveIntegerField(null=True)
    team2_score = models.PositiveIntegerField(null=True)
    winner = models.ForeignKey(Team, related_name='winning_games', on_delete=models.CASCADE, blank=True, null=True)


class GamePlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='game_player')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
