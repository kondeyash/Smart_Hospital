from django.db import models
from patients.models import Patient 
  # if you need to link to Patient

class Bill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Bill for {self.patient.name} - {self.amount}"

class InsuranceClaim(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    insurance_provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ], default='Pending')

    def __str__(self):
        return f"Claim {self.policy_number} - {self.status}"
