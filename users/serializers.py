from rest_framework import serializers
from users.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {"password":{"write_only":True,}}
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {"password":{"write_only":True,}}
        exclude = ['email']

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user