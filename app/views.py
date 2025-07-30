"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Testimonial, Document

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )

def premium(request):
    """Renders the Premium format page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/premium.html',
        {
            'title': 'Формат "Премиум"',
            'year': datetime.now().year,
        }
    )

def praktikum(request):
    """Renders the Praktikum page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/praktikum.html',
        {
            'title': 'Практикум',
            'year': datetime.now().year,
            'message': 'Страница практикума',
        }
    )

def documents(request):
    """Список документов"""
    assert isinstance(request, HttpRequest)
    
    # Получаем все документы из базы данных
    documents_list = Document.objects.all()
    
    return render(
        request,
        'app/documents.html',
        {
            'title': 'Документы',
            'documents': documents_list,
        }
    )



def index(request):
    testimonials = Testimonial.objects.all().order_by('-id')[:10]  # 10 последних отзывов
    context = {
        'testimonials': testimonials,
        'has_testimonials': testimonials.exists()  # Добавляем проверку
    }
    return render(request, 'app/index.html', context)
