from datetime import date

from django.db import models

CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3')
]


class Employees(models.Model):
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    hire_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.TextField(choices=CHOICES, blank=True)
    employment_type = models.TextField(choices=CHOICES, blank=True)


