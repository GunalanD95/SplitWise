import enum 

from django.db import models
from .BaseModel import BaseModel

class ExpenseType(enum.Enum):
    TRANSACTION = 1
    EXPENSE = 2


class Expense(BaseModel):
    description = models.TextField(max_length=255)
    amount = models.IntegerField()
    group  = models.ForeignKey('Group', on_delete=models.PROTECT)
    created_user = models.ForeignKey('User', on_delete=models.PROTECT, related_name='created_user')
    expense_type = models.IntegerField(choices=[(tag.value, tag.name) for tag in ExpenseType])
    created_at = models.DateTimeField()
    
    participants = models.ManyToManyField('User',related_name='participants')