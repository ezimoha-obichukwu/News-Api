from django.contrib import admin
from .models import News


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "source"]
    list_filter = ["author"]
    search_fields = ["title", "author"]
admin.site.register(News, NewsAdmin)
