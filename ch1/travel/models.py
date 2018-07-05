from django.db import models


class Category(models.Model):
    local_category = models.CharField(max_length=10)
    local_img = models.ImageField(default='null', upload_to='local_img')

    def __str__(self):
        return self.local_category

class Post(models.Model):
    local = models.ForeignKey(Category)
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    visited_country = models.CharField(max_length=20)
    interest = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.name

