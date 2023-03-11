from django.db import models

# Create your models here.
from authority.utils import category_directory_path

class FoodCategories(models.Model):
    category_name = models.CharField(max_length=10)
    sort_description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=category_directory_path)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.category_name)
