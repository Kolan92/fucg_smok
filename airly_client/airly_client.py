import requests

class AirlyClient:

    _url = 'https://airapi.airly.eu/v2/measurements/nearest?indexType=AIRLY_CAQI&lat=50.062006&lng=19.940984&maxDistanceKM=3'
    _percent = 0
    _token = ''

    def get_hours_above_limit_in_next_day(self) -> int:
        session = requests.Session()
        response = session.get(self._url, headers={'Accept': 'application/json', 'apikey': self._token })
        
        if response.status_code != 200:
            print('Cant obtain forecast data')
            return None
        
        forecast = response.json()['forecast']
        standards = [f for f in forecast 
            if any(p > self._percent for p in map(lambda x: x['percent'], f['standards']))]

        print(standards)
        print('\n\n\n')
        return len(standards)
        



    def __init__(self, token: str, percent: int):
        self._token = token
        self._percent = percent