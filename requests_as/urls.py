from django.urls import path
from . import views

urlpatterns = [
    path('', views.RequestList.as_view(), name='request-list'),
    path('<int:pk>/', views.RequestDetail.as_view(), name='request-detail'),
]
