from rest_framework import serializers


class AuthenticationSeializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=255,
        style={'placeholder': 'Логин', 'autofocus': True}
    )

    password = serializers.CharField(
        max_length=255,
        style={'input_type': 'password', 'placeholder': 'Пароль'}
    )


        



