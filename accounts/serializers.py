from djoser.serializers import UserCreatePasswordRetypeSerializer

class UserRegistrationPasswordRetypeSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]
