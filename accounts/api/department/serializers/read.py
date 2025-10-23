from rest_framework import serializers

from accounts.api.me.serializers import ReadMeSerializer


class ReadDepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    image = serializers.ImageField()
    owner = ReadMeSerializer()
    users = ReadMeSerializer(many=True)