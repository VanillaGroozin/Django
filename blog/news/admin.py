from django.contrib import admin
from news.models import News, Tag

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','description','status', 'creator', 'created_at']
    list_filter = ('title','status', 'creator', 'created_at')
    search_fields = ['title', "description"]

    class Meta:
        model = News

admin.site.register(News, NewsAdmin)
admin.site.register(Tag)
