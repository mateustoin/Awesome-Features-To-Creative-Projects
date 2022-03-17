# Importa o módulo responsável pela execução das funções
# Import the module responsible for executing the functions
import requests

# Realiza uma requisição GET na url do puzzle fornecida pelo autor da API
# Makes an GET quest on the url given by the API author
result = requests.get('https://api-charadas.herokuapp.com/puzzle?lang=ptbr')

# Imprime o resultado cru e em formato json do request feito
# Print raw and json result from the request
print(result.text)
print(result.json())

# Acessa os campos da questão e resposta do puzzle e armazena em uma variável
# Access question and answer fields and store on a variable
question = result.json()['question']
answer = result.json()['answer']

# Exibe resultado do puzzle
# Shows puzzle results
print(question)
print(answer)