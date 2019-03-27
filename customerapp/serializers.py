from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="customerapp:user-detail")
    class Meta:
        model = User
        fields = ('url','id', 'first_name', 'last_name', 'company_name', 'city', 'state', 'zip', 'email', 'web', 'age')
