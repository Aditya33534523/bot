from djongo import models
from core.models import BaseMongoModel
from django.core.validators import RegexValidator
class Patient(BaseMongoModel):
    phone_validator = RegexValidator(regex=r'^\\+?1?\\d{9,15}$')
    phone_number = models.CharField(validators=[phone_validator], max_length=17, unique=True)
    full_name = models.CharField(max_length=200, blank=True)
    aadhaar_number = models.CharField(max_length=200, blank=True)
    preferred_language = models.CharField(max_length=2, default='en')
    is_verified = models.BooleanField(default=False)
    consent_given = models.BooleanField(default=False)
    district = models.CharField(max_length=100, blank=True)
    class Meta:
        collection_name='patients'

class PatientInteraction(BaseMongoModel):
    patient_phone = models.CharField(max_length=17)
    interaction_type = models.CharField(max_length=20)
    user_message = models.TextField()
    bot_response = models.TextField(blank=True)
    session_id = models.CharField(max_length=100)
    intent_detected = models.CharField(max_length=100, blank=True)
    confidence_score = models.FloatField(null=True, blank=True)
    class Meta:
        collection_name='patient_interactions'
