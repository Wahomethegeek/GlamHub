from django.urls import path
from . import views

urlpatterns = [
    path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail')
]
