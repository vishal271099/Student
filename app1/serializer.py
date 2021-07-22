from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import StudentDetail, GuardianDetail
from rest_framework import exceptions
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

import django.contrib.auth.password_validation as validators


UserModel = get_user_model()


class Guardianserializer(WritableNestedModelSerializer):
    class Meta:
        model = GuardianDetail
        fields = [
            'first_name', 'last_name',
            'relation', 'address', 'mobile_no'
        ]


class Studentserializer(WritableNestedModelSerializer):
    guardians = Guardianserializer(many=True)

    class Meta:
        model = StudentDetail
        fields = [
            'first_name', 'last_name',
            'standard', 'evaluation',
            'city', 'country',
            'active', 'joined_on', 'guardians'
        ]


class AuthTokenSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        msg = ""
        username = attrs.get('username')
        password = attrs.get('password')
        try:
            if username and password:
                user = authenticate(username=username, password=password)
                if not user:
                    msg = "provide credential is incorrect"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "sorry, your password in incorect"
                raise exceptions.ValidationError(msg)
        except Exception as e:
            print(str(e))
            msg = "user not found"
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs


class RegisterSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def create(self, validated_data, **extra_fields):
        user = UserModel.objects.create(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            password=self.validated_data['password'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        confirm_password = self.validated_data['confirm_password']
        user.set_password('password')
        user.save()
        return user

    def validate_password(self, value):
        data = self.get_initial()
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise exceptions.ValidationError('Passwords must  be same')
        return value
