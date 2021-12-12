from django.contrib import admin
from .models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    pass
    # readonly_fields = ('higlighted', )

admin.site.register(Snippet, SnippetAdmin)