from django.db import models


class Agent(models.Model):
    name = models.CharField('Name', max_length=50)
    status = models.BooleanField('Status')
    env = models.CharField('Env', max_length=20)
    version = models.CharField('Version', max_length=5)
    address = models.CharField('Address', max_length=39)


class User(models.Model):
    name = models.CharField('Name', max_length=50, blank=False)
    last_login = models.DateField('last_login', auto_now=True)
    email = models.EmailField('Email address', unique=True)
    password = models.CharField('Password', max_length=50)


class Group(models.Model):
    name = models.CharField('Name', max_length=50)


class Event(models.Model):
    level = models.CharField('Level', max_length=20)
    data = models.TextField('Data')
    arquivado = models.BooleanField('Arquivado')
    date = models.DateField('Date', auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class GroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
