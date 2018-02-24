from rest_framework import serializers
from data_api.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields=('userId','firstName','lastName','phone','emailId','role')