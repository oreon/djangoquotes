from django.db import models

# Create your models here.

from django.db import models
import numpy as np
import datetime as dt



class Client(models.Model):
    name =  models.CharField( max_length=50)
    email = models.EmailField()
    hpd = models.DecimalField(max_digits=3,decimal_places=1)
    rate = models.DecimalField(max_digits=5,decimal_places=1)



class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    fromDate = models.DateTimeField('From')
    toDate = models.DateTimeField('To')
    hours = models.DecimalField(max_digits=5,decimal_places=1)
    absences = models.IntegerField(default=0)

    def weekDays(self):
        return np.busday_count( self.fromDate.date(), self.toDate.date() ) - self.absences

    def totalHours(self): return self.weekDays() * self.client.hpd


    def __str__(self):
        return ' {} {}-{}'.format(self.client.name, self.fromDate, self.toDate )



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
