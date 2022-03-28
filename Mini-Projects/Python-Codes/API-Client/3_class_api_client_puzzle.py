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