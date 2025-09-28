from djongo import models
from core.models import BaseMongoModel
class MedicineRecall(BaseMongoModel):
    recall_id = models.CharField(max_length=50, unique=True)
    medicine_name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    recall_reason = models.TextField()
    severity_level = models.CharField(max_length=10)
    batch_numbers = models.JSONField(default=list)
    recall_date = models.DateTimeField()
    affected_patients_count = models.IntegerField(default=0)
    class Meta:
        collection_name='medicine_recalls'

class PharmacyTransaction(BaseMongoModel):
    patient_phone = models.CharField(max_length=17)
    pharmacy_name = models.CharField(max_length=200)
    medicine_name = models.CharField(max_length=200)
    batch_number = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=200)
    purchase_date = models.DateTimeField()
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        collection_name='pharmacy_transactions'
