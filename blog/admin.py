from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django.utils.safestring import mark_safe

from .models import *

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    # предварительно заполненные поля
    prepopulated_fields = {"slug": ("title",)}
    # добавлена форма для админки ckeditor
    form = PostAdminForm

    # быстро заполнить посты тестовыми данными по образцу
    # save_as = True

    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo',)
    # лист ссылок
    list_display_links = ('id', 'title',)
    # по чему поиск
    search_fields = ('title',)
    # фильтрация по категориям
    list_filter = ('category',)
    # поля для чтения
    readonly_fields = ('views', 'created_at', 'get_photo')
    # как выводить инфо
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'

class CategoryAdmin(admin.ModelAdmin):
    # предварительно заполненные поля
    prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
    # предварительно заполненные поля
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
