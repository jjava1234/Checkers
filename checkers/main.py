import pygame
from checker.game import Game
from checker.board import Board 

def main():
    run = True
    board = Board()
    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()                          
                board.select(pos[0], pos[1])
    
        Game()    
        pygame.display.update()                

    pygame.quit()


main()
