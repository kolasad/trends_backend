from django.contrib import admin
from django.urls import path

from reports.views import TrendReportViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/report/', TrendReportViewSet.as_view()),
]
