from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from users.serializers import PaymentSerializer
from users.models import Payments
from rest_framework.filters import OrderingFilter


class PaymentsListApiView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['method', 'lesson', 'course']
    ordering_fields = ['date_of_pay']
    search_fields = ['method']
