from django.db import models



class Customer_details(models.Model):
    s_no = models.AutoField(primary_key=True, null=False, blank=False)
    customer_name = models.CharField(max_length=100 , null=False, blank=False)
    customer_id = models.CharField(max_length=100, null=False, blank=False)
    passport_id = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.customer_name
    

class UpdatedCustomerDetails(models.Model):
    s_no = models.AutoField(primary_key=True, null=False, blank=False )
    customer_name = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    passport_id = models.CharField(max_length=100)
    # Add any additional fields you need for the new table

    def __str__(self):
        return self.customer_name


# Create your models here.
