import requests

class AirlyClient:

    _url = 'https://airapi.airly.eu/v2/measurements/nearest?indexType=AIRLY_CAQI&lat=50.062006&lng=19.940984&maxDistanceKM=3'
    _token = ''

    def f(self) -> str:
        return 'hello world'
#map(lambda x: x + x, numbers) 
    def get_forecast(self):
        session = requests.Session()
        response = session.get(self._url, headers={'Accept': 'application/json', 'apikey': self._token })
        forecast = response.json()['forecast']
        standards = [s for s in forecast 
            if any(p > 100 for p in map(lambda x: x['percent'], s['standards']))]

        print(standards)
        print('\n\n\n')
        print(len(standards))
        



    def __init__(self, token: str):
        self._token = token