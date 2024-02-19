from django.db import models
from BaseModel import BaseModel

class Group(BaseModel):
    description = models.TextField()
    created_by  = models.ForeignKey('User', on_delete=models.CASCADE)
    
    # each group can will have expenses
    # one  group can have multiple expenses
    # but one expense can be only in one group
    
    members     = models.ManyToManyField('User')