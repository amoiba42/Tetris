import pygame,sys
from game import Game                                                   # type: ignore 
from colors import Color                                                  # type: ignore              
                                                                        #coordinates of the screen are measured from the top-left corner of the screen,unlike the usual cartesian coordinates that start from bottom left corner 
game=Game()
pygame.init()

title_font=pygame.font.SysFont("Monospace",60)                 
score_surface=title_font.render("Score",True,Color.white)               # pygame.font.SysFont(<font>,<size>) returns a font object
score_rect=pygame.Rect(480,120,250,150)
score_value_surface=title_font.render(str(game.score),True,Color.white)
 
next_surface=title_font.render("Next",True,Color.white)               # pygame.font.SysFont(<font>,<size>) returns a font object
next_rect=pygame.Rect(480,370,250,180)

game_over_surface=title_font.render("GameOver",True,Color.white)               # pygame.font.SysFont(<font>,<size>) returns a font object)

screen=pygame.display.set_mode((750,920))                              # pygame.display.set_mode<width>,<height> accepts two values width and height for the screen,
                                                                        # it is for display screen,there can only be one display screen at a time
pygame.display.set_caption("Tetris Game")
GAME_UPDATE=pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,500)                                # pygame.time.set_timer(<event>,<time>) sets a timer for the event passed as an argument, the time is in milliseconds

clock=pygame.time.Clock()

 
while True:                                                             # This is the main loop of the game,which keeps the game running until the user closes the window
    for event in pygame.event.get():                                    # pygame.event.get returns a list of all the events that have occurred since the last time it was called
        if event.type == pygame.QUIT:                                   # if any event calls pygame.QUIT, the game will quit
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:                                # pygame.KEYDOWN is an event that occurs when a key is pressed
            if game.game_over==True:
                game.game_over=False
                game.reset()  
            if event.key==pygame.K_LEFT and game.game_over==False:
                game.move_left()
            if event.key==pygame.K_RIGHT and game.game_over==False:
                game.move_right()
            if event.key==pygame.K_DOWN and game.game_over==False:
                game.move_down()
                game.update_score(0,1)
            if event.key==pygame.K_UP and game.game_over==False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over==False:
            game.move_down() 
                

    # Drawing
    screen.fill(Color.dark_blue)                                         # type: ignore      
    screen.blit(score_surface,(500,50,20,20))   
    pygame.draw.rect(screen,Color.light_blue,score_rect,0,10)                # type: ignore  
    screen.blit(score_value_surface,score_value_surface.get_rect(centerx=score_rect.centerx,centery=score_rect.centery))
    screen.blit(next_surface,(520,300,20,20))
    pygame.draw.rect(screen,Color.light_blue,next_rect,0,10)
    
    if game.game_over==True:  
        screen.blit(game_over_surface,(460,600))
        
    game.draw(screen)                                                   # game.draw draws the game on the screen
    pygame.display.update()                                             # pygame.display.update updates the screen,there can be multiple updates in a single loop
    clock.tick(60)



