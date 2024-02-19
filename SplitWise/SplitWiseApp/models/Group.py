from django.db import models
from .BaseModel import BaseModel

class Group(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    # only one admin for now 
    created_by  = models.ForeignKey('User', on_delete=models.PROTECT,related_name='group_creator')
    
    # each group can will have expenses
    # one  group can have multiple expenses
    # but one expense can be only in one group
    
    group_members     = models.ManyToManyField('User',related_name='group_members')