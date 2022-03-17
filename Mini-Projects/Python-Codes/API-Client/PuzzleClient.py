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