from rest_framework import serializers
from apis.models import User, Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Grade
        fields=["id", 'title']

class UserSerializer(serializers.ModelSerializer):
    grade = GradeSerializer()
    username = serializers.SerializerMethodField()

    def get_username(self, user):
        return user.get_username()

    class Meta:
        model= User
        fields=["id", 'password', 'username', 'first_name', "last_name", 'grade', 'email', 'is_institute', 'is_student']
