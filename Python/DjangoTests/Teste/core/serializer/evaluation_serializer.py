from core.models import Evaluation
from rest_framework import serializers


class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Evaluation

        fields = (
            'name',
            'comment',
            'grade',
        )

    def create(self, validated_data):
        return Evaluation.objects.create(**validated_data)

