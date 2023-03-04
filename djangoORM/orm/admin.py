from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class PCAdmin(admin.ModelAdmin):
    list_display = ('id', 'code','model','speed','ram','hd','cd','price','get_photo')
    list_display_links = ('model', )
    list_filter = ('model', 'speed','ram','hd','cd','price')
    search_fields = ('ram', 'speed')
    fields = ('code','model','speed','ram','hd','cd','price','image')


    def get_photo(self,obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        else:
            return '-'



# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'maker','model','type')
#     list_display_links = ('model', )
#     list_filter = ('maker','model','type')
#     search_fields = ('maker')
#     fields = ('maker','model','type')



admin.site.register(PC,PCAdmin,)
admin.site.register(Printer)
admin.site.register(Product)
admin.site.register(Laptop)


from mptt.admin import DraggableMPTTAdmin
from.models import Rubric

admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title'
    ),
    list_display_links=(
        'indented_title',
    ),

)


