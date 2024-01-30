import pygame

# Initialiser pygame
pygame.init()

# Charger le fichier audio
pygame.mixer.music.load("audio.mp3")

# Lancer la lecture de la musique
pygame.mixer.music.play()

# Attendre la fin de la lecture de la musique
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)