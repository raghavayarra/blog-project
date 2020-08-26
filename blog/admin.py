from django.contrib import admin
from .models import Category,BlogModel,Comment

# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ('id','title','author','created_at','is_apporved')
    list_display_links ='title',
    list_filter = ('created_at','is_apporved')



admin.site.register(Category)
admin.site.register(BlogModel,Admin)
admin.site.register(Comment)