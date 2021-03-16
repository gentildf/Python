#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
print('\033[1mPlayer de música')
pygame.mixer.init()
pygame.mixer.music.load("desafio023.mp3")
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass
