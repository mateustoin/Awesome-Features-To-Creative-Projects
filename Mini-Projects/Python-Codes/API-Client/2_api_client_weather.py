# Importa o módulo responsável pela execução das funções
# Import the module responsible for executing the functions
import requests

# Realiza uma requisição GET na url do weather fornecida pelo autor da API
# Makes an GET quest on the url given by the API author
# https://github.com/robertoduessmann/weather-api
city = 'Sao Paulo'
result = requests.get('https://goweather.herokuapp.com/weather/{city}'.format(city=city))

# Imprime o resultado cru e em formato json do request feito
# Print raw and json result from the request
print(result.json())

# Acessa os campos da temperatura e velocidade do vento e armazena em uma variável
# Access temperature and wind velocity fields and store on a variable
temperature = result.json()['temperature']
wind = result.json()['wind']

# Exibe resultado do puzzle
# Shows puzzle results
print('Temperature: {temperature}'.format(temperature=temperature))
print('Wind: {wind}'.format(wind=wind))