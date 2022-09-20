from django.contrib import admin
from .models import *
from django.forms.widgets import Textarea


# Register your models here.
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    exclude = ['genres']
    fields = [('name', 'description', 'publisher'), 'count', 'authors']
    list_display = ('name', 'description', 'publisher_name', 'publisher_city')
    search_fields = ['name', 'description']

    formfield_overrides = {
        models.TextField: {'widget': Textarea()},
    }

    @admin.display(empty_value='???')
    def publisher_name(self, obj):
        if obj.publisher:
            return obj.publisher.name
        else:
            return ''
    
    @admin.display(empty_value='???')
    def publisher_city(self, obj):
        if obj.publisher:
            return obj.publisher.city
        else:
            return '???'