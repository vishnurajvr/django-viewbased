from rest_framework import serializers

from .models import UserModel



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','name', 'password', 'mail']

    def create(self,validated_data):
        data = UserModel(name=validated_data.get('name'), \
                      password=validated_data.get('password'), \
                      mail=validated_data.get('mail'))
        data.save()
        return UserSerializer(validated_data).data

    def update(self, instance, validated_data):
        user = UserModel.objects.get(pk=instance)
        user.name = validated_data.get('name')
        user.password = validated_data.get('password')
        user.mail = validated_data.get('mail')
        user.save()
        return UserSerializer(validated_data).data
