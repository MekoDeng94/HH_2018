from rest_framework.generics import ListAPIView
from apps.widgets.models.widget import Widget
from apps.widgets.serializers.widget import WidgetSerializer


class WidgetList(ListAPIView):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer
    
    def get_queryset(self):
        qs = super(WidgetList, self).get_queryset()  # Default

        layout = self.request.GET.get('layout')
        if 'layout' in self.kwargs:
            layout = self.kwargs['layout']
        if layout:
            qs = qs.filter(layout__id=layout)

        return qs




