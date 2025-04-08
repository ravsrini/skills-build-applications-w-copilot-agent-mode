from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    members = models.ArrayField(model_container=User)

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.EmbeddedField(model_container=User)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.type} - {self.user.email}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.EmbeddedField(model_container=Team)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.score}"

class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name
