from django.contrib import admin

# Register your models here.
from order.models import Comment, Indent, IndentInventory
class IndentAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['indent_id']
    list_display = ['indent_id', 'customer', 'canteen', 'store', 'comment', 'date_time', 'indent_price', 'indent_state', 'indent_address']
class CommentAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['comment_id', 'score', 'content', 'time']

class IndentInventoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['indent', 'dish', 'dish_num']

admin.site.register(Comment,CommentAdmin)
admin.site.register(Indent,IndentAdmin)
admin.site.register(IndentInventory, IndentInventoryAdmin)