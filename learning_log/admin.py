from django.contrib import admin
from .models import Topic, Entry, Promise

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)
# admin.site.register(Promise)

@admin.register(Promise)
class PromiseAdmin(admin.ModelAdmin):
    fields = ('title', 'description', )
    search_fields = ('title', 'description')
    ordering = ("credatim",)
    list_display = ('title', 'description', 'upddatim')