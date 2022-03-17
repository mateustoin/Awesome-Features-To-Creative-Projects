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