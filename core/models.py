from djongo import models
from datetime import datetime

class BaseMongoModel(models.Model):
    _id = models.ObjectIdField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True