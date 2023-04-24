from django.db import models
import datetime

# Models
from accounts.models import User


# Create your models here.
from products.utils import category_directory_path
from products.utils import food_directory_path
from products.utils import set_menu_directory_path

# Create your models here.

class FoodCategories(models.Model):
    category_name = models.CharField(max_length=30)
    sort_description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=category_directory_path)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.category_name)
    

class MenuFood(models.Model):
    food_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to=food_directory_path, height_field=None, width_field=None, max_length=None)
    description = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default= True)

    def __str__(self):
        return self.food_name

class Foods(models.Model):
    menu_name = models.CharField(max_length=30)
    menu_id = models.CharField(max_length=50, blank=True, null=True)
    foods_items = models.ManyToManyField(MenuFood, related_name='menu_food',blank=True)
    food_catagory = models.ForeignKey(FoodCategories, on_delete=models.CASCADE, related_name='food_category')
    menu_description = models.TextField(blank=True,null=True)
    menu_image = models.ImageField(upload_to=set_menu_directory_path, height_field=None, width_field=None, max_length=None)
    price = models.PositiveIntegerField()
    offer_percentage = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.menu_id or not self.new_price:
            year = str(datetime.date.today().year)[2:4]
            month = str(datetime.date.today().month)
            day = str(datetime.date.today().day)
            self.menu_id = 'E'+year+month+day+str(self.pk).zfill(4)
            self.new_price = int(self.price * (100 - self.offer_percentage) / 100)
            self.save()
       
    def __str__(self):
        return self.menu_name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_user')
    items = models.ForeignKey(Foods, on_delete=models.CASCADE, related_name='cart_items')
    quentity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quentity} X {self.items}"
    
    def get_total(self):
        total = float(self.items.new_price) * self.quentity
        print(total)
        return "{:.2f}".format(total)
    
    def get_total_old(self):
        total = float(self.items.price) * self.quentity
        print(total)
        return "{:.2f}".format(total)

class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=250, blank=True, null=True)
    order_id = models.CharField(max_length=250, blank=True, null=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}'s orders  "

    def get_totals(self):
        total = 0
        for order_item  in self.orderitems.all():
            total += float(order_item.get_total())
        return total

