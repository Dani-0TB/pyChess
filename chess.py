from turtle import back
import pygame, os
from sys import exit

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        board_image = pygame.image.load(os.path.join('Assets/Chess_Board.png')).convert()
        self.image = pygame.transform.rotozoom(board_image, 0,0.7)
        self.rect = self.image.get_rect(center = (640,360))

    def update_board(self):
        pass

class Piece(pygame.sprite.Sprite):
    def __init__(self, type, color, square):
        super().__init__()
        self.type = type
        self.color = color
        self.square = square # Create a variable with a tuple of x and y coordinates
        # Load image
        
        self.image = pygame.image.load(os.path.join(f'Assets/Pieces/{self.type}.png')).convert_alpha()
        self.rect = self.image.get_rect(center = self.square)


def main():
    pygame.init()

    squares = {
    'A1': (394,605),'A2': (465,605), 'A3': (535,605),'A4': (605,605), 
    'A5': (675,605),'A6': (745,605), 'A7': (815,605),'A8': (885,605),
    'B1':(394,535), 'B2':(465,535), 'B3':(535,535), 'B4':(605,535), 
    'B5':(675,535), 'B6':(745,535), 'B7':(815,535), 'B8':(885,535),
    'G1':(394,190), 'G2':(465,190), 'G3':(535,190), 'G4':(605,190), 
    'G5':(675,190), 'G6':(745,190), 'G7':(815,190), 'G8':(885,190),
    'H1':(394,120), 'H2':(465,120), 'H3':(535,120), 'H4':(605,120), 
    'H5':(675,120), 'H6':(745,120), 'H7':(815,120), 'H8':(885,120)}

    display_size = width, height = 1280, 720

    SCREEN = pygame.display.set_mode(display_size)
    pygame.display.set_caption('Welcome to pyChess!')

    color = (84, 132, 156)
    
    clock = pygame.time.Clock()
    FPS = 60

    # Background
    background_surf = pygame.image.load(os.path.join('Assets/background.jpg'))
    background_rect = background_surf.get_rect()

    board = pygame.sprite.GroupSingle()
    board.add(Board())

    pieces = pygame.sprite.Group()
    # White Pawns

    init_pieces(pieces, squares)

    game_on = True
    
    #Main game loop.
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        SCREEN.blit(background_surf,background_rect)
        board.update(SCREEN)
        
        board.draw(SCREEN)

        pieces.draw(SCREEN)

        pygame.display.update()
        clock.tick(FPS)

def init_pieces(pieces, squares):
    for piece in range(1,9):
        pieces.add(Piece('white_pawn', 'white', (squares[f'B{piece}'])))

    white_pieces = [
    'white_rook', 'white_knight','white_bishop',
    'white_king', 'white_queen', 
    'white_bishop','white_knight','white_rook',]
    piece_index = 0
    for piece in white_pieces:
        piece_index += 1
        print(piece)
        pieces.add(Piece(piece, 'white', (squares[f'A{piece_index}'])))


    for piece in range(1,9):
        pieces.add(Piece('black_pawn', 'black', (squares[f'G{piece}'])))
    
    black_pieces = [
    'black_rook', 'black_knight','black_bishop',
    'black_king', 'black_queen', 
    'black_bishop','black_knight','black_rook']
    piece_index = 0
    for piece in black_pieces:
        piece_index += 1
        print(piece)
        pieces.add(Piece(piece, 'black', (squares[f'H{piece_index}'])))
    

if __name__ == '__main__':
    main()