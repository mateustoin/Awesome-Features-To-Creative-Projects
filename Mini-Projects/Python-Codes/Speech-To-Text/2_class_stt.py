# Importa classe criada para facilitar as requisições e resultados
# Import class created to handle requests functions and results
from STTHandler import STTHandler

# Exibe o resultado do puzzle de 2 formas, com a função que mostra automatico e com a captura dos resultados
# Shows results in two ways: with function that shows the result and capturing results and showing manually
def main():
    stt = STTHandler()
    phrase = stt.get_phrase_from_voice()
    
    if phrase != '':
        print('Phrase recognized: {phrase}'.format(phrase=phrase))
    
if __name__ == "__main__":
    main()