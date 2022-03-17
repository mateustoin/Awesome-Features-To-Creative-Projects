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

def main():
    tts = TTSHandler()
    pt_text = 'Testando criação de áudio, funcionando normal!'
    en_text = 'Testing audio creation, it\'s working properly!'
    tts.create_default_audio_to_folder(en_text, filename='en_audio.mp3')
    tts.create_custom_audio_to_folder(pt_text, c_lang='pt', c_tld='com.br', filename='pt_audio.mp3')

if __name__ == "__main__":
    main()