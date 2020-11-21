from rest_framework import serializers
from .models import User


class ReadOnlyUserSerializerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    is_active = serializers.BooleanField(
        required=True,
        help_text='Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.'
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'is_active', 'last_login', 'is_superuser')
        read_only_fields = ('id', 'last_login', 'is_superuser')


class WriteOnlyUserSerializerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    is_active = serializers.BooleanField(
        required=True,
        help_text='Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.'
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'password', 'is_active')
