# Exemplo de Texto para Fala (TTS, do inglês Text-To-Speech)

<!--
    Colocar aqui Thumbnail com link p/ o vídeo do YouTube quando tiver.
-->

> **Descrição da funcionalidade consumir API:**
> Consumir uma API nos dias atuais é um conhecimento extremamente relevante para os mais variados tipos de projetos, integrações com plataformas e variedade nas possibilidades do que você pode fazer. É possível coletar piadas, como faremos nesse exemplo, mas da mesma forma podemos utilizar serviços do Google, AWS, coletar informações sobre notícias, tempo, endereços, entre muitas outras coisas de qualquer lugar do mundo.

## Pré-requisitos

### Python 3.6+

> Utilizado em todos os exemplos

Esses projetos foram testados em dois ambientes diferentes, com Python 3.10.2 e Python 3.8.5. Portanto, é bom ter uma versão atualizada não só para que possamos usurfruir das novidades mas para que também tenhamos certeza de que o próprio Python não será um problema na execução dos exemplos.

Caso não tenha o Python instalado ainda, você pode baixar e seguir as instruções no próprio [site deles](SiteAqui)

### Pacote requests

> Utilizado em todos os exemplos

Esse pacote para Python é o responsável por realizar, como o próprio nome diz, as requisições necessárias para consumir API's, mas não só isso, requisições que podem ser feitas em praticamente qualquer parte da internet. É essencial que tenha ele instalado para a execução dos exemplos. Você pode encontrar as instruções [nesse site](ColocarAquiSiteDoPypi) ou simplesmente executar o comando:

`pip install requests`

## Mini Projetos

Os códigos poderão ser encontrados nesta pasta no github e possuem comentários em inglês e português, pois foram feitos para serem facilmente entendidos. Caso tenha encontrado algum problema ou tenha alguma dúvida, fique a vontade para abrir uma issue nesse repositório!

<details>
<summary>1_api_client.py</summary>

Esse exemplo mostra a forma mais básica e simples de consumir uma API, que também possui uma interface simples. Por aí existem diversos tipos de API's que podem exigir alguns detalhes a mais, mas na essência, todos vão começar dessa forma. Com esse exemplo já é possível consumir boa parte das API's por aí.

```python
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
```

</details>

<details>
<summary>2_class_api_client.py</summary>

Esse exemplo é semelhante ao anterior, no entanto foi feito para que usuários iniciantes possam não só aprender a utilizar a tecnologia, mas também começar a se preocupar com a organização do código e como podem organizá-lo para melhorar seus projetos. A forma como está aqui não necessariamente é correta nem completa, apenas dá uma noção de POO para que o código fique melhor.

- Código que executa as funções criadas
```python
# Importa classe criada para facilitar as requisições e resultados
# Import class created to handle requests functions and results
from PuzzleClient import PuzzleClient

# Exibe o resultado do puzzle de 2 formas, com a função que mostra automatico e com a captura dos resultados
# Shows results in two ways: with function that shows the result and capturing results and showing manually
def main():
    puzzle = PuzzleClient()
    puzzle.make_a_puzzle()
    
    if puzzle.generate_new_puzzle():
        p_question, p_answer = puzzle.get_last_puzzle()
        print(p_question)
        print(p_answer)
    else:
        print('Something went wrong, need to try again')
    
if __name__ == "__main__":
    main()
```

- Código da classe criada
```python
from typing import Tuple
import requests

class PuzzleClient(object):
    def __init__(self):
        # Iniciando apenas com a Url da API
        # Starting only with API Url
        self.joke_url = 'https://api-charadas.herokuapp.com/puzzle?lang=ptbr'
        self.response = None
        self.last_question = ''
        self.las_answer = ''

    def get_last_puzzle(self) -> Tuple(str, str):
        # Retorna o último puzzle capturado pela API
        # Return last puzzle captured from API
        return self.last_question, self.last_answer

    def make_a_puzzle(self) -> None:
        # Gera um novo puzzle e imprime no console
        # Generates new puzzle and prints on console
        self.response = requests.get(self.joke_url)
        
        if self.response.status_code == 201:
            self.last_question = self.response.json()['question']
            self.last_answer = self.response.json()['answer']
            print('Question: ' + self.last_question)
            print('Answer: ' + self.last_answer)
        else:
            print('An error occurred, try again later.')
    
    def generate_new_puzzle(self) -> bool:
        # Gera um novo puzzle para armazenar na classe
        # Generates a new puzzle to store on class
        self.response = requests.get(self.joke_url)
        
        if self.response.status_code == 201:
            self.last_question = self.response.json()['question']
            self.last_answer = self.response.json()['answer']
            return True
        else:
            return False
```

</details>
