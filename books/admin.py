from django.contrib import admin
from .models import Publisher, Author, Book

class PublisherAdmin(admin.ModelAdmin):
    fields = ('name', 'website', 'address', 'city', 'state_province', 'country')
    list_display = ('name', 'city', 'state_province', 'country')
    ordering = ('name', 'state_province', 'country')
    search_fields = ('name', 'city', 'state_province', 'country')


class AuthorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email')
    list_display = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')
    search_fields = ('first_name', 'last_name')
    

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    fields = ('title', 'authors', 'publisher', 'publication_date')
    filter_vertical = ('authors',)
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    ordering = ('-publication_date', 'title')
    # raw_id_fields = ('publisher',) # Used so that not every publisher is loaded into a dropdown box; accpets Publisher ID
    search_fields = ('title', 'publisher', 'publication_date')


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)