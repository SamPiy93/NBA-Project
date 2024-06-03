from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def average_score(self):
        total_score = sum(game.team1_score for game in self.team1_games.all()) + \
                      sum(game.team2_score for game in self.team2_games.all())
        total_games = self.team1_games.count() + self.team2_games.count()

        return (total_score / total_games) if total_games > 0 else 0


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  #TODO: verify this
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

    @property
    def team_won(self):
        if self.team1_score > self.team2_score:
            return self.team1.name
        elif self.team1_score < self.team2_score:
            return self.team2.name
        else:
            return None


class GamePlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='game_player')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
