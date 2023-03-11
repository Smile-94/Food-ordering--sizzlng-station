from django.db import models
from datetime import datetime

# Create your models here.
from authority.utils import category_directory_path
from authority.utils import food_directory_path
from authority.utils import set_menu_directory_path

class FoodCategories(models.Model):
    category_name = models.CharField(max_length=30)
    sort_description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=category_directory_path)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.category_name)
    

class SetMenuFood(models.Model):
    food_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to=food_directory_path, height_field=None, width_field=None, max_length=None)
    description = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default= True)

    def __str__(self):
        return self.food_name

class SetMenu(models.Model):
    menu_name = models.CharField(max_length=30)
    menu_id = models.CharField(max_length=50, blank=True, null=True)
    SetMenuFood = models.ManyToManyField(SetMenuFood, related_name='menu_food')
    food_catagory = models.ForeignKey(FoodCategories, on_delete=models.CASCADE, related_name='food_category')
    menu_description = models.TextField(blank=True,null=True)
    main_image = models.ImageField(upload_to=set_menu_directory_path, height_field=None, width_field=None, max_length=None)
    other_image = models.ImageField(upload_to=set_menu_directory_path, height_field=None, width_field=None, max_length=None)
    price = models.PositiveIntegerField()
    offer_percentage = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.menu_id:
            year = str(datetime.date.today().year)[2:4]
            month = str(datetime.date.today().month)
            day = str(datetime.date.today().day)
            self.menu_id = 'E'+year+month+day+str(self.pk).zfill(4)
            self.save()
        super().save(*args, **kwargs)

        # Calculate the new price based on the offer percentage
        self.new_price = int(self.price * (100 - self.offer_percentage) / 100)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.menu_name


