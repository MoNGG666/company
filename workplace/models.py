from django.db import models


class Branch(models.Model):
    address = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.short_name


class Department(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='departments'
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees'
    )

    def __str__(self):
        return self.full_name



