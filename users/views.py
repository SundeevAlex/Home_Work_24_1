from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from users.serializers import PaymentSerializer, UserSerializer
from users.models import Payments, User
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from users.serializers import CourseBuyingSerializer
from users.services import create_stripe_price, create_stripe_session, create_stripe_product
from users.models import CourseBuying


class PaymentsListApiView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['method', 'lesson', 'course']
    ordering_fields = ['date_of_pay']
    search_fields = ['method']


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDestroyAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class CourseBuyingCreateAPIView(CreateAPIView):

    serializer_class = CourseBuyingSerializer
    queryset = CourseBuying.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        buying = serializer.save(user=self.request.user)
        product = create_stripe_product(buying.course)
        amount_in_rub = buying.amount
        price = create_stripe_price(product=product, amount=amount_in_rub)
        session_id, payment_link = create_stripe_session(price) # (price.id)
        buying.session_id = session_id
        buying.link = payment_link
        buying.save()
