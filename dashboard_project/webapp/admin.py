from django.contrib import admin
from webapp.models import CRUD

# It is used for register our model for visualize our table in django admin panel 

@admin.register(CRUD)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')

    list_display_links = ('title',)

    readonly_fields = ('created_at',)

    ordering = ('-id',)