# Importa classe criada para facilitar as requisições e resultados
# Import class created to handle requests functions and results
from WeatherClient import WeatherClient

# Exibe o resultado do clima da cidade requerida na função
# Shows weather results on required city
def main():
    weather = WeatherClient()
    weather.print_weather_from_city('Santa Rita')
    
if __name__ == "__main__":
    main()