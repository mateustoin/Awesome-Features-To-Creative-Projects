from gtts import gTTS
import time
import os

text = 'Come abacate, filho. Abacate faz bem pra pele.'

file = 'test.mp3'
language = 'pt'

tts = gTTS(text, lang=language, tld='com.br')
tts.save(file)