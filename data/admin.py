from django.contrib import admin
from .models import BlogsLevelOne, BlogsLevelTwo, BlogsLevelThree, BlogsMaxClearance
# Register your models here.

admin.site.register(BlogsLevelOne)
admin.site.register(BlogsLevelTwo)
admin.site.register(BlogsLevelThree)
admin.site.register(BlogsMaxClearance)