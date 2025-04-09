import pygame
import random

pygame.init()

# Configurações de cores e interface
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

# Banco de palavras com dicas
palavras_e_dicas = {
    "cachorro": "Animal de estimação",
    "carro": "Veículo",
    "aviao": "Aeronave",
    "bicicleta": "Veículo de duas rodas",
    "computador": "Dispositivo eletrônico",
}

def desenhar_tela(texto_dica, placar, porcentagem, texto_palavra=None):
    screen.fill(WHITE)
    
    # Placar
    texto_placar = font.render(f"Placar: {placar:.2f}", True, BLACK)
    screen.blit(texto_placar, (10, 10))
    
    # Barra de progresso
    pygame.draw.rect(screen, (200, 200, 200), (100, 50, 600, 20))  # Barra de fundo
    pygame.draw.rect(screen, (0, 150, 0), (100, 50, (porcentagem / 100) * 600, 20))  # Progresso
    texto_progresso = font.render(f"Progresso: {porcentagem:.2f}%", True, BLACK)
    screen.blit(texto_progresso, (100, 80))
    
    # Área principal
    if texto_palavra:
        texto_input = font.render(texto_palavra, True, BLACK)
        screen.blit(texto_input, (WIDTH//2 - texto_input.get_width()//2, HEIGHT//2))
    else:
        texto_instrucao = font.render("Adivinhe a palavra:", True, BLACK)
        screen.blit(texto_instrucao, (WIDTH//2 - texto_instrucao.get_width()//2, HEIGHT//2 - 80))
        
        texto_dica_render = font.render(texto_dica, True, BLACK)
        screen.blit(texto_dica_render, (WIDTH//2 - texto_dica_render.get_width()//2, HEIGHT//2 + 40))
    
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    placar = 0.0
    palavra_sortida = random.choice(list(palavras_e_dicas.keys()))
    dica = f"{palavras_e_dicas[palavra_sortida]} ({len(palavra_sortida)} letras)"
    
    tentativas = 3
    attempts_made = 0
    acertou = False
    input_box = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 100, 200, 50)
    input_text = ''
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    attempts_made += 1
                    # Verifica resposta e atualiza placar
                    if input_text.lower() == palavra_sortida:
                        acertou = True
                        placar += 1
                    else:
                        placar -= 0.33
                    tentativas -= 1
                    input_text = ''
                
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                
                else:
                    input_text += event.unicode
        
        porcentagem = (attempts_made / 3) * 100
        desenhar_tela(dica, placar, porcentagem, input_text if not acertou else None)
        
        # Verifica fim do jogo
        if tentativas <= 0 or acertou:
            # Tela de resultados
            screen.fill(WHITE)
            resultado = "Acertou! +1 ponto" if acertou else "Errou! -1 ponto total"
            texto_resultado = font.render(resultado, True, BLACK)
            screen.blit(texto_resultado, (WIDTH//2 - texto_resultado.get_width()//2, HEIGHT//2 - 100))
            
            texto_palavra = font.render(f"Palavra: {palavra_sortida}", True, BLACK)
            screen.blit(texto_palavra, (WIDTH//2 - texto_palavra.get_width()//2, HEIGHT//2 - 50))
            
            texto_placar = font.render(f"Placar atual: {placar:.2f}", True, BLACK)
            screen.blit(texto_placar, (WIDTH//2 - texto_placar.get_width()//2, HEIGHT//2))
            
            texto_reiniciar = font.render("Jogar novamente? (S/N)", True, BLACK)
            screen.blit(texto_reiniciar, (WIDTH//2 - texto_reiniciar.get_width()//2, HEIGHT//2 + 50))
            
            pygame.display.flip()
            
            # Aguarda decisão do jogador
            esperando = True
            while esperando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        esperando = False
                    
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.lower() == 's':
                            palavra_sortida = random.choice(list(palavras_e_dicas.keys()))
                            dica = f"{palavras_e_dicas[palavra_sortida]} ({len(palavra_sortida)} letras)"
                            tentativas = 3
                            attempts_made = 0
                            acertou = False
                            input_text = ''
                            esperando = False
                        
                        elif event.unicode.lower() == 'n':
                            running = False
                            esperando = False
        
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
