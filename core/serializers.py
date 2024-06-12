from djoser.serializers import UserCreateSerializer as BaseUserVreateSerializers


class UserCreateSerializer(BaseUserVreateSerializers):
    class Meta(BaseUserVreateSerializers.Meta):
        fields = ['id', 'email', 'first_name',
                  'last_name', 'username', 'password']
