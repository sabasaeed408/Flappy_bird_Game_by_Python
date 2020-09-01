import random #for importing random numbers
import sys  #we will use sys.exit to exit the program
import pygame
from pygame.locals import * #basic pygame import
#LOCAL VARIABLE FOR GAME
FPS=32                     #FPS=Frame per second
SCREENWIDTH=289
SCREENHIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHIGHT))
GROUNDY=SCREENHIGHT*0.8
#games sprites which images we use
GAME_SPRITES={}
#gmaes sound is the music we use in game 
GAME_SOUNDS={}
#player,bg,pipe images path
PLAYER='gallery/sprites/bird.png'
BACKGROUND='gallery/sprites/background.png'
PIPE='gallery/sprites/pipe.png'
def welcomeScreen():
        #show welcome image on screen
     playerx=int(SCREENWIDTH/5)
     playery=int((SCREENHIGHT - GAME_SPRITES['player'].get_height())/2)
     messagex=int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
     messagey=int(SCREENHEIGHT*0.13)
     basex=0
     while True:
         for event in pygame.event.get():
             #if user press cross button then close game :)
           if event.type== QUIT or (event.type==KEYDOWN and event.type==K_ESCAPE):
               pygame.quit()
               sys.exit()
            #if user press upkey or space start the game
           elif event.type==kEYDOWN and (event.type==K_SPACE or event.type==K_UP ):
               return
           else:
               SCREEN.blit(GAME_SPRITES['background'],(0,0))
               SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))      
               SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
               SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
               pygame.display.update()
               FPSCLOCK.tick(FPS)
if __name__=="__main__":
    #this is the main point from which our game is start 
 pygame.init()#initilize pygame all modules
 FPSCLOCK=pygame.time.Clock()
 pygame.display.set_caption('FLAPPY BIRD BY SABA SAEED')
 GAME_SPRITES['numbers']=(
    pygame.image.load('gallery/sprites/0.png').convert_alpha(),
    pygame.image.load('gallery/sprites/1.png').convert_alpha(),
    pygame.image.load('gallery/sprites/2.png').convert_alpha(),
    pygame.image.load('gallery/sprites/3.png').convert_alpha(),
    pygame.image.load('gallery/sprites/4.png').convert_alpha(),
    pygame.image.load('gallery/sprites/5.png').convert_alpha(),
    pygame.image.load('gallery/sprites/6.png').convert_alpha(),
    pygame.image.load('gallery/sprites/7.png').convert_alpha(),
    pygame.image.load('gallery/sprites/8.png').convert_alpha(),
    pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )
 GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
 GAME_SPRITES['player']=pygame.image.load(PLAYER).convert
 GAME_SPRITES['message']=pygame.image.load('gallery/sprites/message.png').convert_alpha()
 GAME_SPRITES['base']=pygame.image.load('gallery/sprites/message.png').convert_alpha()
 GAME_SPRITES['pipe']=(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
                      pygame.image.load(PIPE).convert_alpha() )
#GAMES SOUND
 GAME_SOUNDS['die']=pygame.mixer.Sound('gallery/audio/die.wav')
 GAME_SOUNDS['hit']=pygame.mixer.Sound('gallery/audio/hit.wav')
 GAME_SOUNDS['point']=pygame.mixer.Sound('gallery/audio/point.wav')
 GAME_SOUNDS['swoosh']=pygame.mixer.Sound('gallery/audio/point.wav')
 while True:
     welcomeScreen(); #show welcome screen to a player until she press a button
     mainGame();     #this is the main game function
