import pygame
import random
import sys
from pygame.locals import *

# Inicialização do Pygame
pygame.init()

# Configurações da tela (aumentada para 4x4)
TILE_SIZE = 80  # Reduzido para caber 4 colunas
GRID_SIZE = 4   # 4x4 grid
MARGIN = 4
WIDTH = GRID_SIZE * (TILE_SIZE + MARGIN) + MARGIN
HEIGHT = WIDTH + 100  # Espaço para informações
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racha-Cuca 15 Números")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (70, 130, 180)
GREEN = (50, 205, 50)
BACKGROUND = (240, 248, 255)

# Fontes (tamanhos ajustados)
font_large = pygame.font.SysFont('Arial', 36, bold=True)  # Reduzido para caber nos tiles
font_medium = pygame.font.SysFont('Arial', 24)
font_small = pygame.font.SysFont('Arial', 18)

class PuzzleGame:
    def __init__(self):
        self.reset_game()
        
    def reset_game(self):
        # Tabuleiro resolvido (espaço vazio no canto inferior direito)
        self.solution = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]
        
        # Cria cópia do tabuleiro resolvido
        self.board = [row[:] for row in self.solution]
        self.empty_pos = (3, 3)  # Linha, coluna do espaço vazio
        
        # Embaralha o tabuleiro
        self.shuffle_board()
        
        self.moves = 0
        self.game_over = False
    
    def shuffle_board(self):
        """Embaralha o tabuleiro com movimentos válidos"""
        possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # direita, baixo, esquerda, cima
        
        for _ in range(200):  # Mais movimentos para melhor embaralhamento
            move = random.choice(possible_moves)
            new_row = self.empty_pos[0] + move[0]
            new_col = self.empty_pos[1] + move[1]
            
            if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
                # Faz o movimento
                self.board[self.empty_pos[0]][self.empty_pos[1]] = self.board[new_row][new_col]
                self.board[new_row][new_col] = 0
                self.empty_pos = (new_row, new_col)
    
    def draw(self):
        screen.fill(BACKGROUND)
        
        # Desenha o tabuleiro 4x4
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = col * (TILE_SIZE + MARGIN) + MARGIN
                y = row * (TILE_SIZE + MARGIN) + MARGIN
                
                value = self.board[row][col]
                
                if value != 0:
                    pygame.draw.rect(screen, BLUE, (x, y, TILE_SIZE, TILE_SIZE), border_radius=6)
                    pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 2, border_radius=6)
                    
                    # Ajusta tamanho do texto para números com 2 dígitos
                    text = font_large.render(str(value), True, WHITE)
                    text_rect = text.get_rect(center=(x + TILE_SIZE//2, y + TILE_SIZE//2))
                    screen.blit(text, text_rect)
                else:
                    pygame.draw.rect(screen, GRAY, (x, y, TILE_SIZE, TILE_SIZE), border_radius=6)
                    pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 2, border_radius=6)
        
        # Área de informações
        info_y = GRID_SIZE * (TILE_SIZE + MARGIN) + 10
        
        moves_text = font_medium.render(f"Movimentos: {self.moves}", True, BLACK)
        screen.blit(moves_text, (MARGIN, info_y))
        
        if self.game_over:
            congrats_text = font_medium.render("Parabéns! Puzzle resolvido!", True, GREEN)
            screen.blit(congrats_text, (WIDTH//2 - congrats_text.get_width()//2, info_y + 30))
            
            restart_text = font_small.render("Pressione R para reiniciar", True, BLACK)
            screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, info_y + 60))
    
    def move_tile(self, direction):
        """Move uma peça na direção especificada"""
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
            return  # Movimento inválido
        
        # Faz o movimento
        self.board[row][col] = self.board[new_row][new_col]
        self.board[new_row][new_col] = 0
        self.empty_pos = (new_row, new_col)
        self.moves += 1
        
        # Verifica se o jogo acabou
        if self.board == self.solution:
            self.game_over = True
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            
            if event.type == KEYDOWN:
                if event.key == K_r:
                    self.reset_game()
                
                if not self.game_over:
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