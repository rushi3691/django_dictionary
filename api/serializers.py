from rest_framework import serializers
from base.models import Word


class dictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word 
        fields = ['id', 'eng', 'mar']