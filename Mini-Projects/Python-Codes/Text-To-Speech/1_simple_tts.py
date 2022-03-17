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