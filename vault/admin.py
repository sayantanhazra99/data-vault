from django.contrib import admin
from . models import Dataset

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "file", "uploaded_at"]

# This is canother way to register
# admin.site.register(Dataset)
