from django.contrib import admin
from .models import Testimonial, Document
from ckeditor.widgets import CKEditorWidget
from django import forms

# Форма с CKEditor для модели Testimonial
class TestimonialAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(), label='Текст отзыва')
    
    class Meta:
        model = Testimonial
        fields = '__all__'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    form = TestimonialAdminForm  # Используем кастомную форму с CKEditor
    list_display = ('author_name', 'author_position', 'short_text_preview')
    search_fields = ('author_name', 'author_position', 'text')
    list_filter = ('author_position',)
    fields = ('author_name', 'author_position', 'text')
    
    # Добавляем сокращенный просмотр текста в списке
    def short_text_preview(self, obj):
        from django.utils.html import strip_tags
        text = strip_tags(obj.text)  # Удаляем HTML-теги для предпросмотра
        return f"{text[:50]}..." if len(text) > 50 else text
    short_text_preview.short_description = 'Текст отзыва (предпросмотр)'

# Оставляем DocumentAdmin без изменений
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Кортеж с запятой для одного элемента
    search_fields = ('name',)
    fields = ('name', 'file')  # Только имя и файл