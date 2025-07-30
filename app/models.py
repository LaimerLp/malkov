from django.db import models
from ckeditor.fields import RichTextField

class Testimonial(models.Model):
    id = models.BigAutoField(primary_key=True)
    author_name = models.CharField(max_length=100, verbose_name="Имя автора")
    author_position = models.CharField(max_length=100, verbose_name="Должность/статус")
    text = RichTextField(verbose_name='Текст отзыва')  # Заменяем TextField на RichTextField

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-id']

    def __str__(self):
        return f"Отзыв от {self.author_name}"

class Document(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название документа")
    file = models.FileField(upload_to='documents/', verbose_name="Файл")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        ordering = ['-id']  # Сортировка по ID вместо даты

    def __str__(self):
        return self.name
