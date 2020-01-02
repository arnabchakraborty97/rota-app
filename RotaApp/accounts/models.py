from django.contrib.auth.models import User
from django.db import models

ROLE_CHOICES = (
		('ADMIN', 'Admin'),
		('MEMBER', 'Member'),
	)

class Member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')
	phone = models.CharField(max_length=15)
	address = models.TextField()
	date_of_birth = models.DateField()
	date_of_joining = models.DateField()
	blood_group = models.CharField(max_length=5)
	designation = models.CharField(max_length=100)