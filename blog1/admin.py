from django.contrib import admin

from blog1.models import blog


# Register your models here.

@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ['__str__','status']
