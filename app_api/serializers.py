from .models import  Users 
from rest_framework import serializers


class UsersSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=30)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=12)
    password=serializers.CharField(max_length=10)

    def create(self,validated_data):
        print("create method callled...")
        return Users.objects.create(**validated_data)

    def update(self,user,validated_data):
        newUsers = Users(**validated_data)
        newUsers.id = user.id
        newUsers.save()
        return newUsers