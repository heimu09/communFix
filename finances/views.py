from rest_framework import generics
from .models import FinancialReport
from .serializers import FinancialReportSerializer

class FinancialReportList(generics.ListCreateAPIView):
    queryset = FinancialReport.objects.all()
    serializer_class = FinancialReportSerializer

class FinancialReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FinancialReport.objects.all()
    serializer_class = FinancialReportSerializer
