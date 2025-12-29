from django.db import models


class user_journey_record(models.Model):
    user = models.CharField(max_length=255)
    destination_from = models.CharField(max_length=255)
    destination_to = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField(max_length=10)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)