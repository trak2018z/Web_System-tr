from django.db import models
from mongoengine import *

class Choise(EmbeddedDocument):
    choise_text=StringField(max_length=30)
    votes= IntField(default=0)

class Poll(document):
    puestion=StringField(max_length=100)
    data=DateTimeField()
    choises=ListField(EmbeddedDocumentField(Choise))
# Create your models here.
