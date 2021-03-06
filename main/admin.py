from django.contrib import admin
from .models import *
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Articles)
admin.site.register(Comment)
admin.site.register(ArticleImages)
admin.site.register(Publications)
admin.site.register(FeaturedImages)
admin.site.register(Contributors)
