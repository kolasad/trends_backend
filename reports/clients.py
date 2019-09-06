from pytrends.request import TrendReq
from requests.exceptions import ConnectionError


class GoogleTrendsClient:
    def __init__(self):
        self.client = None

    def get_report_data(self, keywords: set):
        try:
            self.client = TrendReq(hl='en-US', tz=360)
        except ConnectionError:
            return 'Connection error, try again later'
        self.client.build_payload(keywords)
        data = self.client.interest_over_time()
        converted = []
        for keyword in keywords:
            converted.append({
                'keyword': keyword,
                'values': [{
                        'date': str(key),
                        'value': value
                    }
                    for key, value in data[keyword].to_dict().items()
                ]
            })
        return converted
