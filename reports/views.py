from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from reports.clients import GoogleTrendsClient


class TrendReportViewSet(APIView):
    def get(self, request):
        keywords = request.GET.get('keywords')
        if not keywords:
            return Response('Please enter keywords', HTTP_400_BAD_REQUEST)
        keywords = set(keywords.split(','))
        client = GoogleTrendsClient()
        return Response(client.get_report_data(keywords=keywords))
