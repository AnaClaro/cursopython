import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pedra, Papel e Tesoura")

# Fonte
font = pygame.font.Font(None, 36)

# Opções
opcoes = ["pedra", "papel", "tesoura"]

# Dimensões e posições dos botões
botao_largura = 150
botao_altura = 50
botao_posicoes = [
    (WIDTH // 2 - botao_largura - 20, HEIGHT // 2 + 150),
    (WIDTH // 2 - botao_largura // 2, HEIGHT // 2 + 150),
    (WIDTH // 2 + 20, HEIGHT // 2 + 150)
]
botao_cores = [GRAY, WHITE, RED]

# Função para determinar o vencedor
def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif (
        (escolha_usuario == "pedra" and escolha_computador == "tesoura") or
        (escolha_usuario == "papel" and escolha_computador == "pedra") or
        (escolha_usuario == "tesoura" and escolha_computador == "papel")
    ):
        return "Usuário"
    else:
        return "Computador"

# Função para desenhar os botões
def desenhar_botoes():
    for i, opcao in enumerate(opcoes):
        x, y = botao_posicoes[i]
        pygame.draw.rect(screen, botao_cores[i], (x, y, botao_largura, botao_altura))
        texto = font.render(opcao.capitalize(), True, BLUE)
        texto_rect = texto.get_rect(center=(x + botao_largura // 2, y + botao_altura // 2))
        screen.blit(texto, texto_rect)

# Função para desenhar a tela
def desenhar_tela(rodada_atual, placar_usuario, placar_computador, mensagem):
    screen.fill(WHITE)

    # Título
    texto_titulo = font.render("Pedra, Papel e Tesoura", True, BLACK)
    texto_rect = texto_titulo.get_rect(center=(WIDTH // 2, 50))
    screen.blit(texto_titulo, texto_rect)

    # Rodada
    texto_rodada = font.render(f"Rodada {rodada_atual}/3", True, BLACK)
    texto_rect = texto_rodada.get_rect(center=(WIDTH // 2, 100))
    screen.blit(texto_rodada, texto_rect)

    # Placar
    texto_placar = font.render(f"Usuário: {placar_usuario} | Computador: {placar_computador}", True, BLACK)
    texto_rect = texto_placar.get_rect(center=(WIDTH // 2, 150))
    screen.blit(texto_placar, texto_rect)

    # Mensagem
    texto_mensagem = font.render(mensagem, True, BLACK)
    texto_rect = texto_mensagem.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(texto_mensagem, texto_rect)

    # Desenhar botões
    desenhar_botoes()

    pygame.display.flip()

def main():
    clock = pygame.time.Clock()

    rodada_atual = 1
    placar_usuario = 0
    placar_computador = 0
    mensagem = "Faça sua escolha!"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi em algum botão
                mouse_pos = event.pos
                for i, (x, y) in enumerate(botao_posicoes):
                    if x <= mouse_pos[0] <= x + botao_largura and y <= mouse_pos[1] <= y + botao_altura:
                        escolha_usuario = opcoes[i]
                        
                        # Escolha do computador
                        escolha_computador = random.choice(opcoes)

                        # Determinar o vencedor
                        vencedor = determinar_vencedor(escolha_usuario, escolha_computador)

                        if vencedor == "Usuário":
                            placar_usuario += 1
                            mensagem = f"Você escolheu {escolha_usuario}, Computador escolheu {escolha_computador}. Você venceu esta rodada!"
                        elif vencedor == "Computador":
                            placar_computador += 1
                            mensagem = f"Você escolheu {escolha_usuario}, Computador escolheu {escolha_computador}. Computador venceu esta rodada!"
                        else:
                            mensagem = f"Você escolheu {escolha_usuario}, Computador escolheu {escolha_computador}. Empate!"

                        rodada_atual += 1

                        # Verifica se o jogo terminou
                        if rodada_atual > 3 or placar_usuario == 2 or placar_computador == 2:
                            if placar_usuario > placar_computador:
                                mensagem = "Parabéns! Você venceu o jogo!"
                            elif placar_computador > placar_usuario:
                                mensagem = "Computador venceu o jogo! Tente novamente."
                            else:
                                mensagem = "O jogo terminou empatado!"
                            
                            desenhar_tela(rodada_atual - 1, placar_usuario, placar_computador, mensagem)
                            
                            pygame.time.wait(3000) # Aguarda antes de reiniciar ou sair
                            
                            rodada_atual = 1
                            placar_usuario = 0
                            placar_computador = 0
                            mensagem = "Faça sua escolha!"

        desenhar_tela(rodada_atual, placar_usuario, placar_computador, mensagem)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
