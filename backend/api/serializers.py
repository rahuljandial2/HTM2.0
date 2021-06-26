from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault
from rest_framework.authtoken.models import Token


from .models import Task, Profile

class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64, required=False)
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), required=False)
    
    class Meta:
        model   = Task
        fields  = '__all__'
        # read_only_fields = ('')

    def validate(self, attrs):
        if not self.instance:
            if 'name' not in attrs:
                raise serializers.ValidationError("A Task Reauires a 'name' to be inialized")
        return attrs




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
            Profile.objects.create(user=user)

            token, _ = Token.objects.get_or_create(user=user)
            attrs['token'] = token


        else:
            mes = "You are required to provide a 'Username', 'Email', and 'Password'."
            raise serializers.ValidationError(mes)


        return attrs

class UserDetailSerializer(serializers.ModelField):



    class Meta:
        models = User
        fields = ['username', 'email', 'profile']