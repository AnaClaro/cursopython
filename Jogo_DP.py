import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Adivinhação de Palavras")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND = (240, 240, 240)
YELLOW = (255, 255, 0)
PROGRESS_BAR_BG = (200, 200, 200)
PROGRESS_BAR_FG = (0, 150, 0)

# Fontes
title_font = pygame.font.SysFont('Arial', 40, bold=True)
main_font = pygame.font.SysFont('Arial', 32)
hint_font = pygame.font.SysFont('Arial', 24, italic=True)
score_font = pygame.font.SysFont('Arial', 28, bold=True)
progress_font = pygame.font.SysFont('Arial', 20)

# Banco de palavras e dicas
word_hints = {
    "python": ["Linguagem de programação", "Nome de uma cobra", "Usado em inteligência artificial"],
    "gato": ["Animal doméstico", "Tem bigodes", "Dizem que tem 7 vidas"],
    "sol": ["Fonte de luz natural", "Estrela mais próxima da Terra", "Dá nome a um sistema"],
    "livro": ["Contém páginas", "Fonte de conhecimento", "Pode ser físico ou digital"],
    "musica": ["Arte dos sons", "Tem ritmo e melodia", "Pode ser cantada ou instrumental"],
    "futebol": ["Esporte com bola", "Jogado em times de 11", "Esporte mais popular do mundo"],
    "chocolate": ["Doce popular", "Pode ser ao leite ou amargo", "Ingrediente de muitos doces"],
    "computador": ["Máquina eletrônica", "Processa informações", "Pode ser desktop ou notebook"]
}

class WordGame:
    def __init__(self):
        self.running = True
        self.user_text = ""
        self.input_active = True
        self.score = 0.0
        self.score_updated = False
        self.total_questions = 0  # Inicializado aqui
        self.correct_answers = 0  # Inicializado aqui
        self.reset_game()  # Chamado depois de inicializar todas as variáveis
    
    def reset_game(self):
        self.secret_word, self.hints = random.choice(list(word_hints.items()))
        self.attempts = 3
        self.current_hint = 0
        self.game_over = False
        self.won = False
        self.user_text = ""
        self.score_updated = False
        self.total_questions += 1
    
    def update_score(self):
        if not self.score_updated:
            if self.won:
                self.score += 1.0
                self.correct_answers += 1
            else:
                self.score -= 0.33
                self.score = max(0, self.score)
            self.score_updated = True
    
    def draw_progress_bar(self):
        # Calcula a porcentagem baseada nas tentativas usadas
        progress = (3 - self.attempts) * 33.33
        progress = min(100, progress)
        
        # Barra de progresso
        bar_width = 600
        bar_height = 20
        bar_x = (WIDTH - bar_width) // 2
        bar_y = HEIGHT - 40
        
        # Fundo da barra
        pygame.draw.rect(screen, PROGRESS_BAR_BG, (bar_x, bar_y, bar_width, bar_height))
        
        # Progresso atual
        filled_width = (progress / 100) * bar_width
        pygame.draw.rect(screen, PROGRESS_BAR_FG, (bar_x, bar_y, filled_width, bar_height))
        
        # Texto de porcentagem
        progress_text = progress_font.render(f"Progresso: {progress:.2f}%", True, BLACK)
        screen.blit(progress_text, (bar_x, bar_y - 25))
        
        # Estatísticas (com verificação para evitar divisão por zero)
        accuracy = 0
        if self.total_questions > 0:
            accuracy = (self.correct_answers / self.total_questions) * 100
        
        stats_text = progress_font.render(
            f"Palavras: {self.total_questions} | Acertos: {self.correct_answers} | Taxa de acerto: {accuracy:.1f}%", 
            True, BLACK
        )
        screen.blit(stats_text, (bar_x, bar_y - 55))
    
    def draw(self):
        screen.fill(BACKGROUND)
        
        # Placar
        score_text = score_font.render(f"Pontuação: {self.score:.2f}", True, YELLOW)
        screen.blit(score_text, (20, 20))
        
        # Título
        title = title_font.render("Adivinhe a Palavra", True, BLUE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))
        
        # Informação sobre a palavra
        word_length = len(self.secret_word)
        length_info = main_font.render(f"A palavra tem {word_length} letras", True, BLACK)
        screen.blit(length_info, (WIDTH//2 - length_info.get_width()//2, 120))
        
        # Dica
        hint_text = f"Dica {self.current_hint + 1}/3: {self.hints[self.current_hint]}"
        hint = hint_font.render(hint_text, True, BLACK)
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, 170))
        
        # Tentativas restantes
        attempts = main_font.render(f"Tentativas restantes: {self.attempts}", True, BLACK)
        screen.blit(attempts, (WIDTH//2 - attempts.get_width()//2, 220))
        
        # Input do usuário
        input_rect = pygame.Rect(WIDTH//2 - 150, 270, 300, 50)
        pygame.draw.rect(screen, BLACK, input_rect, 2)
        
        text_surface = main_font.render(self.user_text, True, BLACK)
        screen.blit(text_surface, (input_rect.x + 10, input_rect.y + 10))
        
        # Mensagem de resultado
        if self.game_over:
            if self.won:
                result = main_font.render("Parabéns! Você acertou!", True, GREEN)
            else:
                result = main_font.render(f"Game Over! A palavra era: {self.secret_word}", True, RED)
            
            screen.blit(result, (WIDTH//2 - result.get_width()//2, 350))
            
            # Atualiza a pontuação apenas uma vez
            self.update_score()
            
            # Botão para jogar novamente
            pygame.draw.rect(screen, BLUE, (WIDTH//2 - 100, 420, 200, 50))
            again = main_font.render("Jogar Novamente", True, WHITE)
            screen.blit(again, (WIDTH//2 - again.get_width()//2, 430))
            
            # Botão para sair
            pygame.draw.rect(screen, RED, (WIDTH//2 - 100, 490, 200, 50))
            quit_text = main_font.render("Sair", True, WHITE)
            screen.blit(quit_text, (WIDTH//2 - quit_text.get_width()//2, 500))
        
        # Barra de progresso
        self.draw_progress_bar()
    
    def check_guess(self):
        if self.user_text.lower() == self.secret_word.lower():
            self.won = True
            self.game_over = True
        else:
            self.attempts -= 1
            self.current_hint = min(self.current_hint + 1, 2)
            
            if self.attempts <= 0:
                self.game_over = True
        
        self.user_text = ""
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
                mouse_pos = pygame.mouse.get_pos()
                
                # Verifica se clicou no botão "Jogar Novamente"
                if WIDTH//2 - 100 <= mouse_pos[0] <= WIDTH//2 + 100:
                    if 420 <= mouse_pos[1] <= 470:
                        self.reset_game()
                    elif 490 <= mouse_pos[1] <= 540:
                        self.running = False
            
            if not self.game_over and self.input_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.check_guess()
                    elif event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode
    
    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

# Inicia o jogo
if __name__ == "__main__":
    game = WordGame()
    game.run()