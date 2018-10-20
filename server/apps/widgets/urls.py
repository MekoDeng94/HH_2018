from django.urls import path
from apps.widgets.views.widget import WidgetList


urlpatterns = [
    path(r'widgets', WidgetList.as_view()),
]
