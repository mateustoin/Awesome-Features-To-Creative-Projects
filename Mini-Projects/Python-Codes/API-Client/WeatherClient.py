import requests

class WeatherClient(object):
    def __init__(self):
        # Iniciando apenas com a Url da API
        # Starting only with API Url
        self.weather_url = 'https://goweather.herokuapp.com/weather/'
        self.response = None
        self.last_city = ''
        self.last_temperature = ''
        self.last_wind = ''

    def get_last_weather_info(self):
        # Retorna o último clima capturado pela API
        # Return last weather captured from API
        return [self.last_city, self.last_temperature, self.last_wind]

    def print_weather_from_city(self, city) -> None:
        self.response = requests.get(self.weather_url + city)
        
        if self.response.status_code == 200:
            self.last_city = city
            self.last_temperature = self.response.json()['temperature']
            self.last_wind = self.response.json()['wind']
            print('{city} Temperature: {temperature}'.format(city=self.last_city, temperature=self.last_temperature))
            print('{city} Wind: {wind}'.format(city=self.last_city, wind=self.last_wind))
        else:
            print('An error occurred, try again later.')
