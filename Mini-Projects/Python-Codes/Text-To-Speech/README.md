# Exemplo de Texto para Fala (TTS, do inglês Text-To-Speech)

<!--
    Colocar aqui Thumbnail com link p/ o vídeo do YouTube quando tiver.
-->

> **Descrição da funcionalidade TTS:**
> O TTS é uma tecnologia que utiliza como base um texto, que pode vir de uma String ou até de um arquivo de texto, por exemplo, para transformar em fala, que pode ser executada a partir de um arquivo de áudio.

## Pré-requisitos

### Python 3.6+

> Utilizado em todos os exemplos

Esses projetos foram testados em dois ambientes diferentes, com Python 3.10.2 e Python 3.8.5. Portanto, é bom ter uma versão atualizada não só para que possamos usurfruir das novidades mas para que também tenhamos certeza de que o próprio Python não será um problema na execução dos exemplos.

Caso não tenha o Python instalado ainda, você pode baixar e seguir as instruções no próprio [site deles](SiteAqui)

### Pacote gTTS

> Utilizado em todos os exemplos

Esse pacote para Python é o responsável por realizar a "mágica" de transformar o texto para fala. É essencial que tenha ele instalado para a execução dos exemplos. Você pode encontrar as instruções [nesse site](ColocarAquiSiteDoPypi) ou simplesmente executar o comando:

`pip install gTTS`

### Pacote Pygame

> Utilizando apenas em '2_play_tts.py'

A instalação do pygamme não é obrigatória. Esse pacote é bem famoso e bastante utilizado em diversos tipos de projetos em Python, como criação de jogos e até interfaces simples. Utilizaremos ele apenas para executar os sons de falas gerados pelo exemplo do TTS. Ele possui diversos módulos internos e um deles é o Mixer, que permite que arquivos de áudio possam ser executados. Você pode encontrar mais informações [nesse site](ColocarAqui) ou simplesmente instalar com o comando:

`pip install pygame`

Caso tenha algum problema com a instalação, recomendo que olhe o [repositório oficial do projeto](ColocarRepositorioAqui), que possui mais detalhes relacionados a dependências e do que o pacote pode precisar a mais para funcionar.

## Mini Projetos - Exemplos de códigos

Os códigos poderão ser encontrados nesta pasta no github e possuem comentários em inglês e português, pois foram feitos para serem facilmente entendidos. Caso tenha encontrado algum problema ou tenha alguma dúvida, fique a vontade para abrir uma issue nesse repositório!

<details>
<summary>1_simple_tts.py</summary>

Esse exemplo possui o exemplo mais básico para utilizar o tts, onde você só precisa especificar apenas o texto e língua, tendo um arquivo mp3 salvo no final.

```python
# Importa o módulo responsável pela execução das funções
# Import the module responsible for executing the functions
from gtts import gTTS

# Texto que será transformado em áudio
# Text that will be transformed into audio
text = 'Come abacate, filho. Abacate faz bem pra pele.'

# Criando o objeto com texto, língua e domínio da língua
# Creating the object with text and language. If you don't specify any 'lang' and 'tld', english is default
tts = gTTS(text, lang='pt', tld='com.br')

# Salva o arquivo de áudio criado
# Saves the audio file created
tts.save('audio_file.mp3')
```

</details>

<details>
<summary>2_play_tts.py</summary>

Esse exemplo é semelhante ao anterior, no entanto possui algumas linhas a mais, para que o áudio seja executado depois de ser gerado, para que o usuário consiga executar o programa e escutar diretamente.

```python
# Importa os módulos responsáveis pela execução das funções
# Import the modules responsible for executing the functions
from gtts import gTTS
import pygame

# Texto que será transformado em áudio
# Text that will be transformed into audio
text = 'Come abacate, filho. Abacate faz bem pra pele.'

# Criando o objeto com texto, língua e domínio da língua
# Creating the object with text and language. If you don't specify any 'lang' and 'tld', english is default
tts = gTTS(text, lang='pt', tld='com.br')

# Salva o arquivo de áudio criado
# Saves the audio file created
tts.save('audio_file.mp3')

# Inicializa módulo de reprodução e música, carrega áudio e inicia execução
# Start playback and music module, load audio and start playing
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('audio_file.mp3')
pygame.mixer.music.play()

# Espera até a reprodução do áudio acabar, então encerra reprodução
# Waits until audio playback ends, then finish reproduction
while pygame.mixer.music.get_busy() == True:
    continue

pygame.mixer.music.stop()
```

</details>

<details>
<summary>3_class_tts.py</summary>

Esse exemplo é apenas para mostrar um exemplo de código um pouco mais organizado, para que usuários iniciantes tenham uma noção de como podem organizar melhor o código para melhorar a qualidade dos seus projetos. O código necessariamente não possui nada novo, apenas reestruturado de uma forma simples e organizada.

- Código que executa as funções criadas: 
```python
# Importando módulo criado na mesma pasta para organização do código
# Importing module created on the same folder to organize code
from TTSHandler import TTSHandler

def main():
    tts = TTSHandler()
    pt_text = 'Testando criação de áudio, funcionando normal!'
    en_text = 'Testing audio creation, it\'s working properly!'
    tts.create_default_audio_to_folder(en_text, filename='en_audio.mp3')
    tts.create_custom_audio_to_folder(pt_text, c_lang='pt', c_tld='com.br', filename='pt_audio.mp3')

if __name__ == "__main__":
    main()
```

- Código da classe criada: 
```python
from io import BytesIO
from gtts import gTTS

class TTSHandler:
    # Inicializando classe e a língua padrão é inglês
    # Initializing class and default language is english
    def __init__(self, d_lang: str='en', d_tld: str='com', d_filename: str='audio.mp3'):
        self.lang = d_lang
        self.tld = d_tld
        self.filename = d_filename

    # Se quiser mudar a linguagem padrão da classe
    # If you want to change dafult language
    def change_default_lang(self, d_lang: str, d_tld: str) -> None:
        self.lang = d_lang
        self.tld = d_tld

    # Cria audio e salva na pasta utilizando a linguagem padrão da classe
    # Creates audio and save on the same folder using default language
    def create_default_audio_to_folder(self, text: str, filename: str=None) -> bool:
        tts = gTTS(text=text, lang=self.lang, tld=self.tld)

        try:
            if filename != None:
                tts.save(filename)
            else:
                tts.save(self.filename)
            return True
        except:
            print("Error")
            return False

    # Cria e retorna um objeto de bytes do áudio criado, usando linguagem padrão da classe
    # Creates and returns bytes as a object from the audio created, using default language
    def create_default_bytes_audio_fp(self, text: str) -> BytesIO():
        mp3_fp = BytesIO()
        tts = gTTS(text=text, lang=self.lang, tld=self.tld)

        try:
            tts.write_to_fp(mp3_fp)
            return mp3_fp
        except:
            print("Error writing to FP file, returning empty bytes")
            return mp3_fp

    # Cria audio e salva na pasta utilizando a linguagem definida na função
    # Creates audio and save on the same folder using language defined on function
    def create_custom_audio_to_folder(self, text: str, c_lang: str,
                                            c_tld: str, filename: str=None) -> bool:
        tts = gTTS(text=text, lang=c_lang, tld=c_tld)

        try:
            if filename != None:
                tts.save(filename)
            else:
                tts.save(self.filename)
            return True
        except:
            print("Error")
            return False
```

</details>
