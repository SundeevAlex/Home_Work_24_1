from rest_framework.serializers import ModelSerializer
from users.models import Payments, User, CourseBuying


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CourseBuyingSerializer(ModelSerializer):
    class Meta:
        model = CourseBuying
        fields = "__all__"
