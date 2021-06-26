from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault
from rest_framework.authtoken.models import Token


from .models import Task



class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email    = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, trim_whitespace=False)
    token    = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token')

    def validate_creds(self, username, password):
        
        return True

    def validate(self, attrs):
        username    = attrs.get('username')
        email       = attrs.get('email')
        password    = attrs.get('password')

        if username and email and password:
            if User.objects.filter(username=username).exists() :
                mes = "A user of this 'Username' already exists. The 'Username' should be unique."
                raise serializers.ValidationError(mes)

            elif not self.validate_creds(username, password):
                mes = "You Must Provide a Reasonable 'Username' and Secure 'Password'."
                raise serializers.ValidationError(mes)

            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
            attrs['token'] = token


        else:
            mes = "You are required to provide a 'Username', 'Email', and 'Password'."
            raise serializers.ValidationError(mes)


        return attrs

