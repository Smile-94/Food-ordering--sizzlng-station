from django.db import models


class BookTable(models.Model):
    party_size = models.PositiveBigIntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=17)
    email = models.EmailField(max_length=254)
    occasion = models.CharField(max_length=15,blank=True, null=True)
    messages = models.TextField(blank=True, null=True)
    table_no = models.PositiveIntegerField(default=0)
    review_message = models.TextField()
    confirm_status = models.BooleanField(default= False)
    is_active = models.BooleanField(default=True)

