from djoser.serializers import UserCreateSerializer as BaseUserVreateSerializers
from djoser.serializers import UserSerializer as BaseUserSeializers

from store.models import Customer


class UserCreateSerializer(BaseUserVreateSerializers):
    class Meta(BaseUserVreateSerializers.Meta):
        fields = ['id', 'email', 'first_name',
                  'last_name', 'username', 'password']


class UserSerializer(BaseUserSeializers):
    class Meta(BaseUserSeializers.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
