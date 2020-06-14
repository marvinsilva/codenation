from django.db import models
from django.core import validators


class Agent(models.Model):
    name = models.CharField('Agent Name', max_length=50)
    status = models.BooleanField('Agent Status')
    env = models.CharField('Agent Environment', max_length=20)
    version = models.CharField('Agent Version', max_length=5)
    address = models.GenericIPAddressField('Agent IP Addess', protocol='IPV4', max_length=39)


class User(models.Model):
    name = models.CharField('User Name', max_length=50)
    last_login = models.DateTimeField('User Last Login', auto_now=True)
    email = models.EmailField('User Email')
    password = models.CharField('User Password', max_length=50, validators=[validators.MinLengthValidator(8)])


class Event(models.Model):
    CRITICAL = 'CRT'
    DEBUG = 'DBG'
    ERROR = 'ERR'
    WARNING = 'WRN'
    INFO = 'INF'

    LEVEL_CHOICES = [
        (CRITICAL, 'Critical'),
        (DEBUG, 'Debug'),
        (ERROR, 'Error'),
        (WARNING, 'Warning'),
        (INFO, 'Info')
    ]

    level = models.CharField('Event Level', max_length=20, choices=LEVEL_CHOICES, default=INFO)
    data = models.TextField('Event Data')
    arquivado = models.BooleanField('Event Arquivado')
    date = models.DateField('Date', auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.deletion.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING)


class Group(models.Model):
    name = models.CharField('Name', max_length=50)


class GroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING)
    group = models.ForeignKey(Group, on_delete=models.deletion.DO_NOTHING)
