from rest_framework import serializers
from .models import UsersAPI


class UserApiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.CharField()
    password = serializers.CharField()


    def create(self, validated_data):
        return UsersAPI.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)

        instance.save()
        return instance