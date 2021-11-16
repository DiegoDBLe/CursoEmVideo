#FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex019.mp3')
pygame.mixer_music.play()
pygame.event.wait()
