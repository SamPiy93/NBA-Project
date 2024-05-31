from django.db import models

# Create your models here.
class User(models.Model):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('coach', 'Coach'),
        ('player', 'Player')
    )
    username = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100, choices=USER_TYPES)


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Player(models.Model):
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    average_score = models.FloatField(default=0)
    game_count = models.IntegerField(default=0)


class Team(models.Model):
    coach = models.OneToOneField(Coach, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    average_score = models.FloatField(default=0)
    players = models.ManyToManyField('Player', related_name='teams')


class Game(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_1_games')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_2_games')
    team_1_score = models.IntegerField(default=0)
    team_2_score = models.IntegerField(default=0)
