from django.contrib import admin
from .models import *
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Articles)
admin.site.register(Comment)
admin.site.register(ArticleImages)

