import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("audio.wav")
pygame.mixer.music.play()

time.sleep(5)