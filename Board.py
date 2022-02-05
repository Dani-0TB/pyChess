import pygame, os
class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        board_image = pygame.image.load(os.path.join('Assets/Chess_Board.png')).convert()
        self.image = pygame.transform.rotozoom(board_image, 0,0.7)
        self.rect = self.image.get_rect(center = (640,360))

    def update_board(self):
        pass