# Register your models here.

from django.contrib import admin
from models import BookInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'btitle','bcover_img','bauthor','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10

admin.site.register(BookInfo,BookInfoAdmin)


