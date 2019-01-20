from django.urls import path

from . import views

urlpatterns = [
    path('', views.generate, name='generate'),
    path('generated/<str:filename>', views.serve_image, name='generate'),
]
