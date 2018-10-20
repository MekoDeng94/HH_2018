from rest_framework import serializers
from apps.widgets.models.widget import Widget


class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = '__all__'