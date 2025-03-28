from django.db import models


class AccommodationSpecialist(models.Model):
    specialist_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)

class Accommodation(models.Model):
    accommodation_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(
        max_length=20,
        choices=[('Room', 'Room'), ('Flat', 'Flat')]
    )
    address = models.TextField()
    location = models.CharField(max_length=100)
    area = models.IntegerField()  # e.g., square feet
    monthly_rental = models.IntegerField()  # e.g., in HK$
    surcharge = models.CharField(max_length=200)
    facilities = models.TextField()
    vancancies = models.CharField(max_length=10)
    special_conditions = models.TextField()
    environment = models.TextField()
    other_info = models.TextField()
    contact = models.CharField(max_length=100)
    posting_start_date = models.DateField()
    posting_end_date = models.DateField()

class Reservation(models.Model):
    reservation_id = models.CharField(max_length=50, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('Active', 'Active'), ('Cancelled', 'Cancelled')]
    )

class Notification(models.Model):
    notification_id = models.CharField(max_length=50, primary_key=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length=20,
        choices=[('Reservation', 'Reservation'), ('Cancellation', 'Cancellation')]
    )
