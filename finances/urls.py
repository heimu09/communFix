from django.urls import path
from . import views

urlpatterns = [
    path('', views.FinancialReportList.as_view(), name='financialreport-list'),
    path('<int:pk>/', views.FinancialReportDetail.as_view(), name='financialreport-detail'),
]
