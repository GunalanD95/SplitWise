from BaseModel import BaseModel
from django.db import models


class User(BaseModel):
    user_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    hashed_password = models.CharField(max_length=255)