from django.contrib import admin

from .models import Author, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "available")
    list_filter = ("available"),
    search_fields = ("title", "author"),
    # list_editable = ('available',)
    ordering = ('title',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
