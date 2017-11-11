from rest_framework import serializers


class ContainerSerializer(serializers.Serializer):
    container_id = serializers.CharField(read_only=True, allow_blank=False, allow_null=False)
    tag = serializers.CharField(allow_blank=True)
    image = serializers.CharField(allow_blank=False)
    command = serializers.CharField(allow_blank=True)
    created = serializers.CharField(allow_blank=False)
    status = serializers.CharField(allow_blank=False)
    state = serializers.CharField(allow_blank=False)
    ports = serializers.CharField(allow_blank=True)
    names = serializers.CharField(allow_blank=True)
    ip = serializers.CharField(read_only=True)
    image_id = serializers.CharField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
