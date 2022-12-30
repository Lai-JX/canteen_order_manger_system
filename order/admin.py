from django.contrib import admin

# Register your models here.
from order.models import Comment, Indent, IndentInventory
class IndentAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['indent_id']
    list_display = ['indent_id', 'canteen', 'store']
admin.site.register(Comment)
admin.site.register(Indent,IndentAdmin)
admin.site.register(IndentInventory)