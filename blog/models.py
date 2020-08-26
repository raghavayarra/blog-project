from django.db import models
from datetime import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class BlogModel(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to='photos')
    author = models.CharField(max_length=100)
    created_at = models.DateField(default=datetime.now,blank=True)
    descriptipon =models.TextField()
    is_apporved = models.BooleanField(blank=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogModel,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateField(default=datetime.now,blank=True)
    is_apporved = models.BooleanField(blank=False)



    def __str__(self):
        return self.name
    
