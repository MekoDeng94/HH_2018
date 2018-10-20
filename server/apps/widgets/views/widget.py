from rest_framework.generics import ListAPIView
from apps.widgets.models.widget import Widget
from apps.widgets.serializers.widget import WidgetSerializer

class WidgetList(ListAPIView):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer
    






