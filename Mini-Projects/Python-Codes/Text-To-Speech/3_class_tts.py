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