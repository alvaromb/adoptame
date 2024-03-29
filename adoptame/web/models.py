from django.db import models
from django.contrib.auth.models import User

# This contains all possible states of adoption: e.g. adopted, not adopted...
class State(models.Model):
    desc = models.CharField(max_length=300)
    def __unicode__(self):
        return self.desc

class Race(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Location(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=400)
    animal_assoc = models.BooleanField()
    description = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    def __unicode__(self):
        return self.name
    def is_assoc(self):
        return self.animal_assoc

class Animal(models.Model):
    name = models.CharField(max_length=300)
    age = models.PositiveSmallIntegerField()
    race = models.ForeignKey(Race)
    description = models.TextField()
    state = models.ForeignKey(State)
    pub_date = models.DateTimeField(auto_now_add=True)
    adoption_limit = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(Location)
    publisher = models.ForeignKey(User)
    def __unicode__(self):
        return self.name

class RequestMessage(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True)
    animal = models.ForeignKey(Animal)
    def __unicode__(self):
        return self.text + self.author + self.pub_date
    
