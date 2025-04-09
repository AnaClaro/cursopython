import pygame
import random
import sys
from pygame.locals import *

# Inicialização do Pygame
pygame.init()

# Configurações da tela (aumentada em 30% na vertical)
TILE_SIZE = 100
GRID_SIZE = 3
MARGIN = 5
WIDTH = GRID_SIZE * (TILE_SIZE + MARGIN) + MARGIN
BASE_HEIGHT = WIDTH
HEIGHT = int(BASE_HEIGHT * 1.3)  # Aumento de 30% na altura
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racha-Cuca Numérico")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (70, 130, 180)
GREEN = (50, 205, 50)
BACKGROUND = (240, 248, 255)  # Azul alice

# Fontes
font_large = pygame.font.SysFont('Arial', 48, bold=True)
font_medium = pygame.font.SysFont('Arial', 28)
font_small = pygame.font.SysFont('Arial', 20)

class PuzzleGame:
    def __init__(self):
        self.reset_game()
        
    def reset_game(self):
        self.solution = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.board = [row[:] for row in self.solution]
        self.empty_pos = (2, 2)
        self.shuffle_board()
        self.moves = 0
        self.game_over = False
    
    def shuffle_board(self):
        possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for _ in range(100):
            move = random.choice(possible_moves)
            new_row = self.empty_pos[0] + move[0]
            new_col = self.empty_pos[1] + move[1]
            if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
                self.board[self.empty_pos[0]][self.empty_pos[1]] = self.board[new_row][new_col]
                self.board[new_row][new_col] = 0
                self.empty_pos = (new_row, new_col)
    
    def draw(self):
        screen.fill(BACKGROUND)
        
        # Desenha o tabuleiro
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = col * (TILE_SIZE + MARGIN) + MARGIN
                y = row * (TILE_SIZE + MARGIN) + MARGIN
                value = self.board[row][col]
                
                if value != 0:
                    pygame.draw.rect(screen, BLUE, (x, y, TILE_SIZE, TILE_SIZE), border_radius=8)
                    pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 2, border_radius=8)
                    text = font_large.render(str(value), True, WHITE)
                    text_rect = text.get_rect(center=(x + TILE_SIZE//2, y + TILE_SIZE//2))
                    screen.blit(text, text_rect)
                else:
                    pygame.draw.rect(screen, GRAY, (x, y, TILE_SIZE, TILE_SIZE), border_radius=8)
                    pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 2, border_radius=8)
        
        # Área de informações (com mais espaço)
        info_y = BASE_HEIGHT + 20  # Começa após o tabuleiro
        
        moves_text = font_medium.render(f"Movimentos: {self.moves}", True, BLACK)
        screen.blit(moves_text, (MARGIN, info_y))
        
        if self.game_over:
            congrats_y = info_y + 40
            restart_y = info_y + 80
            
            congrats_text = font_medium.render("Parabéns! Você completou!", True, GREEN)
            screen.blit(congrats_text, (WIDTH//2 - congrats_text.get_width()//2, congrats_y))
            
            restart_text = font_small.render("Pressione R para reiniciar", True, BLACK)
            screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, restart_y))
    
    def move_tile(self, direction):
        if self.game_over:
            return
        
        row, col = self.empty_pos
        new_row, new_col = row, col
        
        if direction == "up" and row < GRID_SIZE - 1:
            new_row = row + 1
        elif direction == "down" and row > 0:
            new_row = row - 1
        elif direction == "left" and col < GRID_SIZE - 1:
            new_col = col + 1
        elif direction == "right" and col > 0:
            new_col = col - 1
        else:
            return
        
        self.board[row][col] = self.board[new_row][new_col]
        self.board[new_row][new_col] = 0
        self.empty_pos = (new_row, new_col)
        self.moves += 1
        
        if self.board == self.solution:
            self.game_over = True
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            
            if event.type == KEYDOWN:
                if event.key == K_r:
                    self.reset_game()
                elif not self.game_over:
                    if event.key == K_UP:
                        self.move_tile("up")
                    elif event.key == K_DOWN:
                        self.move_tile("down")
                    elif event.key == K_LEFT:
                        self.move_tile("left")
                    elif event.key == K_RIGHT:
                        self.move_tile("right")
        
        return True
    
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            running = self.handle_events()
            self.draw()
            pygame.display.flip()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = PuzzleGame()
    game.run()