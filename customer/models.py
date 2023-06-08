from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Customer/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    national_id = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=50, null=True)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


class ClaimForm(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    second_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=False)
    purchase_date = models.DateField(null=True)
    policy_type = models.CharField(max_length=150, null=True)
    claim_details = models.TextField(max_length=300, null=True)
    amount = models.IntegerField()




