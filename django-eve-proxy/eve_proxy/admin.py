from django.contrib import admin
from eve_proxy.models import CachedDocument

class CachedDocumentAdmin(admin.ModelAdmin):
    model = CachedDocument
    list_display = ('url_path', 'time_retrieved', 'cached_until')
    verbose_name = 'Cached Document'
    verbose_name_plural = 'Cached Documents'
admin.site.register(CachedDocument, CachedDocumentAdmin)
