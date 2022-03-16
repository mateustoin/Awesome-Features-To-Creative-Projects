from gtts import gTTS
import pygame
import time
import os

text = 'Come abacate, filho. Abacate faz bem pra pele.'

file = 'test.mp3'
language = 'pt'

tts = gTTS(text, lang=language, tld='com.br')
tts.save(file)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

time.sleep(10)

pygame.mixer.music.stop()
