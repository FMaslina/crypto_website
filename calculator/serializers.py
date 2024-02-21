from rest_framework import serializers

from calculator.models import Percent


class PercentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Percent
        fields = '__all__'
