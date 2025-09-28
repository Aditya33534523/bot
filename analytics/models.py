from djongo import models
from core.models import BaseMongoModel

class HealthInsight(BaseMongoModel):
    insight_type = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.TextField()
    data = models.JSONField()
    date_range_start = models.DateField()
    date_range_end = models.DateField()
    
    class Meta:
        collection_name = 'health_insights'