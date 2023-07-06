from datetime import date

from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from python_p10.authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    birth_date = serializers.DateField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'can_be_contacted', 'can_be_data_shared', 'password', 'birth_date']

    def create(self, validated_data):
        if relativedelta(date.today(), validated_data['birth_date']).years < 15:
            raise serializers.ValidationError('You must be at least 15 years old to create an account.')
        del validated_data['birth_date']
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
