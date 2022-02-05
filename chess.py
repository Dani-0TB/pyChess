import pygame, os
from sys import exit
from Board import *
from Piece import *


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

    clock = pygame.time.Clock()
    FPS = 60

    # Background
    background_surf = pygame.image.load(os.path.join('Assets/background.jpg'))
    background_rect = background_surf.get_rect()

    board = pygame.sprite.GroupSingle()
    board.add(Board())

    pieces = pygame.sprite.Group()

    move_sound = pygame.mixer.Sound(os.path.join('Assets/Sound/move.wav'))
    capture_sound = pygame.mixer.Sound(os.path.join('Assets/Sound/capture.wav'))
    # White Pawns

    init_pieces(pieces, squares)
    pieces_on_board = []

    game_on = True
    
    #Main game loop.
    while game_on:
        pieces_on_board = []
        for piece in pieces:
            if not piece.picked_up:
                pieces_on_board.append(piece)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Pice Movement logic
            if event.type == pygame.MOUSEBUTTONDOWN:
                for piece in pieces:
                    if piece.rect.collidepoint(pygame.mouse.get_pos()): piece.picked_up = True
            if event.type == pygame.MOUSEBUTTONUP:
                for piece in pieces:
                    # Simple Capture Mechanic.
                    if piece.picked_up:
                        for piece_2 in pieces_on_board:
                            if piece.rect.collidepoint(piece_2.rect.center): piece_2.remove()

                    if piece.rect.collidepoint(pygame.mouse.get_pos()) and piece.picked_up: piece.picked_up = False
                             
            # Reset Game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: init_pieces(pieces, squares)
        piece_list = []
        for piece in pieces:
            piece_list.append(piece)
            
        SCREEN.blit(background_surf,background_rect)
        board.update(SCREEN)
        
        board.draw(SCREEN)
        pieces.update()
        pieces.draw(SCREEN)
        pygame.display.update()
        clock.tick(FPS)

def init_pieces(pieces, squares):
    pieces.empty()
    for piece in range(1,9):
        pieces.add(Piece('white_pawn', 'white', (squares[f'B{piece}'])))

    white_pieces = [
    'white_rook', 'white_knight','white_bishop',
    'white_queen', 'white_king',
    'white_bishop','white_knight','white_rook',]
    piece_index = 0
    for piece in white_pieces:
        piece_index += 1
        pieces.add(Piece(piece, 'white', (squares[f'A{piece_index}'])))


    for piece in range(1,9):
        pieces.add(Piece('black_pawn', 'black', (squares[f'G{piece}'])))
    
    black_pieces = [
    'black_rook', 'black_knight','black_bishop',
    'black_queen', 'black_king',
    'black_bishop','black_knight','black_rook']
    piece_index = 0
    for piece in black_pieces:
        piece_index += 1
        pieces.add(Piece(piece, 'black', (squares[f'H{piece_index}'])))
    

if __name__ == '__main__':
    main()