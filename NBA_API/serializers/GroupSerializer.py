from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
        serializer for Group model
    """

    class Meta:
        model = Group
        fields = ["url", "name"]
