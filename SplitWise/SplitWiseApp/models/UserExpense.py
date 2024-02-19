from django.db import models
from .BaseModel import BaseModel

class ExpensePayingUser(BaseModel):
    # expense paying user
    user    = models.ForeignKey('User', on_delete=models.PROTECT)
    expense = models.ForeignKey('Expense', on_delete=models.CASCADE)
    amount  = models.DecimalField(max_digits=10, decimal_places=2)
    
class ExpenseOwingUser(BaseModel):
    # expense owing user
    user    = models.ForeignKey('User', on_delete=models.PROTECT)
    expense = models.ForeignKey('Expense', on_delete=models.CASCADE)
    amount  = models.DecimalField(max_digits=10, decimal_places=2)