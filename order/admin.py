from django.contrib import admin

# Register your models here.
from order.models import Comment, Indent, IndentInventory

admin.site.register(Comment)
admin.site.register(Indent)
admin.site.register(IndentInventory)