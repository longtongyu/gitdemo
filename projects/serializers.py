from rest_framework import serializers

class ProjectSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    leader = serializers.CharField(max_length = 20)
    is_execute = serializers.BooleanField()
