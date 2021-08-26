from django.db import models


# Create your models here.
class Match(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__ (self):
        return self.name

class Team(models.Model):
    identifier = models.AutoField(primary_key=True)
    teamName = models.CharField(max_length=200)
    logouri = models.ImageField(upload_to='images/')
    club_state = models.CharField(max_length=200)
    players = models.ManyToManyField('Player', related_name='players')
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__ (self):
        return self.teamName

class Player(models.Model):
    identifier = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    imageUri = models.ImageField(upload_to='images/')
    player_jersey_number = models.IntegerField()
    country = models.CharField(max_length=200)
    matches = models.ForeignKey(Match, on_delete=models.CASCADE)
    run = models.IntegerField()
    highest_scores = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__ (self):
        return self.firstName


class Winner(models.Model):
    matchdate = models.DateField(auto_now_add=False,null=True, blank=True)
    matches = models.ForeignKey(Match, on_delete=models.CASCADE)
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='team_a')
    team_b = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_b')
    score_a = models.IntegerField()
    score_b = models.IntegerField()
    winner_team = models.ForeignKey(Team, on_delete=models.CASCADE)



