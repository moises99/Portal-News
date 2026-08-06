from django.contrib import admin
from news_app import models
# Register your models here.

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','url_noticia','url_imagen',)
    list_filter = ('titulo',)
    list_per_page = 25
    ordering = ('-id',)
    search_fields = ('titulo','id',)

    def __str__(self) ->str:
        return f'{self.titulo}'
