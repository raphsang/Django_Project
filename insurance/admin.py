from django.contrib import admin
from django.contrib import admin
from .models import Policy
from .actions import generate_pdf
from customer.models import Customer, ClaimForm
from django.http import HttpResponse
import csv
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import csv


class PolicyAdmin(admin.ModelAdmin):
    list_display = ['category', 'policy_name']


admin.site.register(Policy, PolicyAdmin)


def generate_report(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="my_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'username', 'address', 'mobile'])

    for obj in queryset:
        writer.writerow([obj.id, obj.username, obj.address, obj.mobile])

    return response


# Define the admin class for your model
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'address', 'mobile')
    actions = [generate_report, generate_pdf]


# Register your model and its admin class with the admin site
admin.site.register(Customer, CustomerAdmin)


class ClaimFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'purchase_date', 'policy_type', 'claim_details', 'amount')
    actions = [generate_report, generate_pdf]
