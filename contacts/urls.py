from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactList.as_view(), name='contact-list'),
    path('<int:pk>/', views.ContactDetail.as_view(), name='contact-detail'),
]
