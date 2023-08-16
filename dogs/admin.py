from typing import Any, Optional
from django.contrib import admin
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField, ModelForm
from django.http.request import HttpRequest

from .models import Dog, GalleryImage

class ImageInLine(admin.TabularInline):
    model = GalleryImage
    extra = 1


class DogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "breed", "dob", "sex", "weight", "profile_pic"]}),
        ("Compatibility", {"fields": ["dog_friendly", "cat_friendly", "child_friendly", "house_broken"]}),
        (None, {"fields": ["description"]}),
        ("Other", {"fields": ["adopted", "hidden", "notice", "bonded_pair"]})
    ]
    inlines = [ImageInLine]

    list_display = ["id", "name", "breed", "dob", "sex", "adopted"]
    list_filter = ["adopted"]
    search_fields = ["name"]


# Register your models here.
admin.site.register(Dog, DogAdmin)