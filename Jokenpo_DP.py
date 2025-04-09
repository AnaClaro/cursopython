import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 900, 700  # Aumentei a altura para acomodar melhor as mensagens
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pedra, Papel e Tesoura")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND = (240, 240, 240)
YELLOW = (255, 255, 0)
GRAY = (150, 150, 150)

# Fontes
title_font = pygame.font.SysFont('Arial', 42, bold=True)
main_font = pygame.font.SysFont('Arial', 34)
button_font = pygame.font.SysFont('Arial', 26, bold=True)
result_font = pygame.font.SysFont('Arial', 30, bold=True)

# Opções do jogo
OPTIONS = ['pedra', 'papel', 'tesoura']
BEATS = {
    'pedra': 'tesoura',
    'papel': 'pedra',
    'tesoura': 'papel'
}

class RockPaperScissors:
    def __init__(self):
        self.reset_game()
        self.running = True
        self.awaiting_restart_decision = False
    
    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.round = 1
        self.game_over = False
        self.player_choice = None
        self.computer_choice = None
        self.round_result = ""
        self.game_result = ""
        self.awaiting_restart_decision = False
    
    def computer_play(self):
        return random.choice(OPTIONS)
    
    def determine_winner(self, player, computer):
        if player == computer:
            return "Empate!"
        elif BEATS[player] == computer:
            self.player_score += 1
            return "Você venceu esta rodada!"
        else:
            self.computer_score += 1
            return "Computador venceu esta rodada!"
    
    def play_round(self, player_choice):
        self.player_choice = player_choice
        self.computer_choice = self.computer_play()
        self.round_result = self.determine_winner(self.player_choice, self.computer_choice)
        
        if self.round >= 3 or self.player_score >= 2 or self.computer_score >= 2:
            self.game_over = True
            if self.player_score > self.computer_score:
                self.game_result = "Você venceu o jogo!"
            elif self.computer_score > self.player_score:
                self.game_result = "Computador venceu o jogo!"
            else:
                self.game_result = "O jogo terminou em empate!"
            self.awaiting_restart_decision = True
        else:
            self.round += 1
    
    def draw(self):
        screen.fill(BACKGROUND)
        
        # Título
        title = title_font.render("Pedra, Papel e Tesoura", True, BLUE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))
        
        # Placar
        score_text = main_font.render(f"Você {self.player_score} x {self.computer_score} Computador", True, BLACK)
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 100))
        
        # Rodada atual
        round_text = main_font.render(f"Rodada: {self.round}/3", True, BLACK)
        screen.blit(round_text, (WIDTH//2 - round_text.get_width()//2, 150))
        
        # Botões de escolha
        if not self.game_over:
            button_width, button_height = 220, 90
            spacing = 40
            button_y = 280
            
            # Pedra
            pygame.draw.rect(screen, GRAY, (WIDTH//2 - button_width*1.5 - spacing, button_y, button_width, button_height), border_radius=10)
            pygame.draw.rect(screen, BLACK, (WIDTH//2 - button_width*1.5 - spacing, button_y, button_width, button_height), 3, border_radius=10)
            pedra = button_font.render("PEDRA", True, BLUE)
            screen.blit(pedra, (WIDTH//2 - button_width*1.5 - spacing + button_width//2 - pedra.get_width()//2, 
                              button_y + button_height//2 - pedra.get_height()//2))
            
            # Papel
            pygame.draw.rect(screen, WHITE, (WIDTH//2 - button_width//2, button_y, button_width, button_height), border_radius=10)
            pygame.draw.rect(screen, BLACK, (WIDTH//2 - button_width//2, button_y, button_width, button_height), 3, border_radius=10)
            papel = button_font.render("PAPEL", True, BLUE)
            screen.blit(papel, (WIDTH//2 - button_width//2 + button_width//2 - papel.get_width()//2, 
                              button_y + button_height//2 - papel.get_height()//2))
            
            # Tesoura
            pygame.draw.rect(screen, RED, (WIDTH//2 + button_width//2 + spacing, button_y, button_width, button_height), border_radius=10)
            pygame.draw.rect(screen, BLACK, (WIDTH//2 + button_width//2 + spacing, button_y, button_width, button_height), 3, border_radius=10)
            tesoura = button_font.render("TESOURA", True, BLUE)
            screen.blit(tesoura, (WIDTH//2 + button_width//2 + spacing + button_width//2 - tesoura.get_width()//2, 
                                button_y + button_height//2 - tesoura.get_height()//2))
        
        # Resultados (agora em linhas separadas)
        if self.player_choice and self.computer_choice:
            # Escolhas do jogador e computador
            player_choice_text = main_font.render(f"Você escolheu: {self.player_choice.upper()}", True, BLACK)
            screen.blit(player_choice_text, (WIDTH//2 - player_choice_text.get_width()//2, 400))
            
            computer_choice_text = main_font.render(f"Computador escolheu: {self.computer_choice.upper()}", True, BLACK)
            screen.blit(computer_choice_text, (WIDTH//2 - computer_choice_text.get_width()//2, 450))
            
            # Resultado da rodada
            result = result_font.render(self.round_result, True, 
                                     GREEN if "Você" in self.round_result else 
                                     RED if "Computador" in self.round_result else BLACK)
            screen.blit(result, (WIDTH//2 - result.get_width()//2, 500))
        
        # Resultado final do jogo
        if self.game_over:
            game_result = result_font.render(self.game_result, True, 
                                           GREEN if "Você" in self.game_result else 
                                           RED if "Computador" in self.game_result else BLACK)
            screen.blit(game_result, (WIDTH//2 - game_result.get_width()//2, 550))
            
            # Mensagem para reiniciar
            restart_text = main_font.render("Deseja jogar novamente? (S/N)", True, BLUE)
            screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, 600))
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN and self.awaiting_restart_decision:
                if event.key == pygame.K_s:
                    self.reset_game()
                elif event.key == pygame.K_n:
                    self.running = False
            
            if not self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                button_width, button_height = 220, 90
                spacing = 40
                button_y = 280
                
                # Pedra
                if (WIDTH//2 - button_width*1.5 - spacing <= mouse_pos[0] <= WIDTH//2 - button_width*0.5 - spacing and 
                    button_y <= mouse_pos[1] <= button_y + button_height):
                    self.play_round('pedra')
                
                # Papel
                elif (WIDTH//2 - button_width//2 <= mouse_pos[0] <= WIDTH//2 + button_width//2 and 
                      button_y <= mouse_pos[1] <= button_y + button_height):
                    self.play_round('papel')
                
                # Tesoura
                elif (WIDTH//2 + button_width//2 + spacing <= mouse_pos[0] <= WIDTH//2 + button_width*1.5 + spacing and 
                      button_y <= mouse_pos[1] <= button_y + button_height):
                    self.play_round('tesoura')
    
    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

# Inicia o jogo
if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()