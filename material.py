import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
hod = []
eat = []
board = pygame.image.load('settings/material/board.png')
parad = pygame.image.load('settings/material/parad.png')
ww = pygame.image.load('settings/material/WINW.png')
wb = pygame.image.load('settings/material/WINB.png')
pSH = pygame.image.load('settings/particl/pSH.png')

king = pygame.image.load('settings/material/King.png')
slon = pygame.image.load('settings/material/Slon.png')
pesh = pygame.image.load('settings/material/Pesh.png')
tura = pygame.image.load('settings/material/Lad.png')
ferz = pygame.image.load('settings/material/Ferz.png')
kon = pygame.image.load('settings/material/Kon.png')

peshW = pygame.image.load('settings/material/PeshW.png')
ladW = pygame.image.load('settings/material/LadW.png')
konW = pygame.image.load('settings/material/konW.png')
slonW = pygame.image.load('settings/material/SlonW.png')
ferzW = pygame.image.load('settings/material/FerzW.png')
kingW = pygame.image.load('settings/material/KingW.png')

king.set_colorkey(WHITE)
slon.set_colorkey(WHITE)
pesh.set_colorkey(WHITE)
tura.set_colorkey(WHITE)
ferz.set_colorkey(WHITE)
kon.set_colorkey(WHITE)

peshW.set_colorkey(BLACK)
ladW.set_colorkey(BLACK)
konW.set_colorkey(BLACK)
slonW.set_colorkey(BLACK)
ferzW.set_colorkey(BLACK)
kingW.set_colorkey(BLACK)

pSH.set_colorkey(WHITE)

for i in range(2):
    file = 'settings/particl/pE{}.png'.format(i)
    img = pygame.image.load(file)
    img.set_colorkey(WHITE)
    eat.append(img)
for i in range(4):
    file = 'settings/particl/p{}.png'.format(i)
    img = pygame.image.load(file)
    img.set_colorkey(WHITE)
    hod.append(img)