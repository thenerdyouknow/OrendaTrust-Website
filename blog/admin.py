from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','pub_date','image','body','summary']


admin.site.register(Blog, BlogAdmin)
