from django.db import models

class FinancialReport(models.Model):
    date = models.DateField()
    income = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
