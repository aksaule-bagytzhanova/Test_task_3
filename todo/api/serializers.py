import sys

from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User, update_last_login
from django.contrib.auth import get_user_model, authenticate
from rest_framework.settings import api_settings

from .models import Task
import django.contrib.auth.password_validation as validators
from django.core import exceptions
UserModel = get_user_model()
from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text

from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError


class TaskCreateSerilizer(serializers.ModelSerializer):
    done = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = '__all__'


class TaskShowSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('user', 'title', 'text', 'deadline', 'done')


class TaskDoneSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('done')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'email'
        )

    def validate_password(self, value):
        try:
            validators.validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])

        user.is_active = False
        user.save()
        return user

    def update(self, instance, validated_data):
        validated_data = self.check_for_unique_email(validated_data)
        user = super().update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user


