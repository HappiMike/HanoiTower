
import pygame

from pygame.locals import *

import time

pygame.init()

##  ------------------ Setup de pantalla -------------------- ##
WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
pygame.display.set_caption(" Torre Hanoi ")

## ----------------- Settings generales ------------------- ##
FPS = 240
showFps = False

Anillos = 5   #GLOBAL

font = pygame.font.Font('arial.ttf',32)



## ----------------------- Colores ------------------------  ##
BLANCO = (255, 255, 255)
GRIS = (60, 60, 90)
NEGRO = (0, 0, 0)

COLORS = [(160,253,90),(200,180,90),(130,75,55),(34,139,34),(107,142,35),(233,150,122),(186,85,211),(0,139,139),(178,34,34),(10,10,85)]


## ------------------------ Hanoi -------------------------- ##

class Board:
    def __init__(self):
        self.Towers = [[*range(Anillos, 0,-1)],[],[]]
        self.Solution = []
    
    def Move(self, origin, destination):
        global Towers
        self.Towers[destination].append(self.Towers[origin][-1])
        self.Towers[origin].pop()

    def Solve(self,n, origin, destination, extra):
        if n == 0:
            return
        self.Solve(n-1, origin, extra, destination)
        self.Solution.append((origin, destination))
        print(self.Solution[-1])
        self.Solve(n-1, extra, destination, origin)

Hanoi = Board()

Hanoi.Solve(Anillos, 0, 2, 1)


## ----------------------- Screen Update --------------------##

def ImprimirPantalla():
    WIN.fill(GRIS)

    pygame.draw.rect(WIN, (35,30,55), pygame.Rect(30,70,200,600)) #Left Banner

    pygame.draw.rect(WIN, NEGRO, pygame.Rect(400,500,800,40)) # Base

    pygame.draw.rect(WIN, NEGRO, pygame.Rect(575,240,33,270)) # Pillar 0
    pygame.draw.rect(WIN, NEGRO, pygame.Rect(775,240,33,270)) # Pillar 1
    pygame.draw.rect(WIN, NEGRO, pygame.Rect(975,240,33,270)) # Pillar 2

    #Anillos
    i = 1
    for tower in Hanoi.Towers:
        for ring in range(len(tower)):
            pygame.draw.rect(WIN, COLORS[tower[ring]], pygame.Rect((360+ 200*i - tower[ring]*8,450-ring*50, 60+tower[ring]*16,50)))
            ringnum = font.render(str(tower[ring]), False, pygame.Color('white'))
            WIN.blit(ringnum, (380+ 200*i,450-ring*50 +8))
        i += 1
            
    


    pygame.display.update()


##  ----------------- CONTROLADOR MAIN --------------------- ##

def main():
    clock =  pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        ## Quit event handler ^



        ##Loop v

        for x in Hanoi.Solution:
            ImprimirPantalla()
            time.sleep(1)
            Hanoi.Move(x[0], x[1])
        ImprimirPantalla()
        time.sleep(3)
        exit()

 

    pygame.quit()



## -------- Inicializador de main y verificacion de archivo ---------- ##
if __name__ == "__main__":
    main()

    print("\n ######## Fin Del Programa ######## \n")
