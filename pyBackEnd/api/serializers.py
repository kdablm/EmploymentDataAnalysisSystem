from rest_framework import serializers

from .models import User


class HelloSerializer(serializers.Serializer):
    """示例序列化器"""

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(max_length=100, required=False)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'createTime', 'avatar', 'work', 'address', 'workExperience', 'educational',
                  'password', 'userName']
