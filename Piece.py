import pygame, os
class Piece(pygame.sprite.Sprite):
    def __init__(self, type, color, square):
        super().__init__()
        self.type = type
        self.color = color
        self.square = square # Create a variable with a tuple of x and y coordinates
        self.picked_up = False
        # Load image
        
        self.image = pygame.image.load(os.path.join(f'Assets/Pieces/{self.type}.png')).convert_alpha()
        self.rect = self.image.get_rect(center = self.square)

    def move_piece(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.picked_up:
            self.rect.center = mouse_pos

    def remove(self):
        self.kill()

    def update(self):
        self.move_piece()

