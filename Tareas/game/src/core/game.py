import pygame
import random
from core.config import Config
from entities.player import Player
from builder.enemy_builder import EnemyBuilder
from builder.director import EnemyDirector
from utils.check_collision import check_collision

pygame.init()

# Configuration
config = Config()
WIDTH, HEIGHT = config.get('WIDTH'), config.get('HEIGHT')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')

# Función para mostrar el menú de selección de naves
def show_ship_selection_menu():
    font = pygame.font.Font(None, 36)
    options = [
        {"name": "Nave Rápida", "PLAYER_SPEED": 9, "BULLET_SPEED": 12, "SCORE_MULT": 1.0},
        {"name": "Nave Equilibrada", "PLAYER_SPEED": 7, "BULLET_SPEED": 10, "SCORE_MULT": 1.2},
        {"name": "Nave Poderosa", "PLAYER_SPEED": 5, "BULLET_SPEED": 7, "SCORE_MULT": 1.5},
    ]
    selected_option = 0

    while True:
        screen.fill((0, 0, 0))
        title_text = font.render('Selecciona tu nave', True, (255, 255, 255))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        for i, option in enumerate(options):
            color = (255, 255, 255) if i == selected_option else (100, 100, 100)
            option_text = font.render(option["name"], True, color)
            screen.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, HEIGHT // 2 + i * 40))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected_option]

def show_game_over_screen(score):
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    game_over_text = font.render('Game Over', True, (255, 0, 0))
    score_text = small_font.render(f'Score: {score}', True, (255, 255, 255))
    restart_text = small_font.render('Press R to Restart or Q to Quit', True, (255, 255, 255))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 1.5))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Reiniciar el juego
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

# Mostrar el menú de selección de naves y obtener la configuración seleccionada
selected_ship = show_ship_selection_menu()
PLAYER_SPEED, BULLET_SPEED, SCORE_MULT = selected_ship["PLAYER_SPEED"], selected_ship["BULLET_SPEED"], selected_ship["SCORE_MULT"]

# Jugador
player = Player(WIDTH // 2, HEIGHT - 80, '../assets/images/player.png', BULLET_SPEED, PLAYER_SPEED, SCORE_MULT)

# Enemies
director = EnemyDirector()
builder = EnemyBuilder()

enemies = [
    director.construct_enemy(builder, 'normal'),
    director.construct_enemy(builder, 'fast'),
    director.construct_enemy(builder, 'strong')
]

bullets = []

enemy_speed = 1
enemy_spawn_timer = 0
shoot_delay = 500  # 500 ms = .5 segundos
last_shot_time = 0  # Momento del último disparo
score = 0 # Puntuación
font = pygame.font.Font(None, 36) # Fuente para el texto de puntuación

running = True
while running:
    pygame.time.delay(30)
    current_time = pygame.time.get_ticks()
    screen.fill((0, 0, 0))
    # Renderizar texto de puntuación en la esquina superior izquierda
    score_text = font.render(f'Score: {score}', True, (255, 255, 255)) # Texto de puntuación
    screen.blit(score_text, (10, 10))
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Controles
    keys = pygame.key.get_pressed()
    player.move(keys, WIDTH)
    
    if keys[pygame.K_SPACE] and current_time - last_shot_time >= shoot_delay:
        bullets.append(player.shoot())
        last_shot_time = current_time
    
    for bullet in bullets[:]:
        bullet.move()
        if bullet.y < 0:
            bullets.remove(bullet)
    
    for enemy in enemies[:]:
        enemy.move()
        if check_collision(player, enemy):
            if not show_game_over_screen(score):
                running = False
            else:
                # Reiniciar el juego
                player = Player(WIDTH // 2, HEIGHT - 80, '../assets/images/player.png', BULLET_SPEED, PLAYER_SPEED, SCORE_MULT)
                enemies = [
                    director.construct_enemy(builder, 'normal'),
                    director.construct_enemy(builder, 'fast'),
                    director.construct_enemy(builder, 'strong')
                ]
                bullets = []
                score = 0
                enemy_spawn_timer = 0
                last_shot_time = 0
    
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if check_collision(bullet, enemy):
                score += enemy.points * player.scoreMult
                bullets.remove(bullet)
                enemies.remove(enemy)
                break
    
    enemy_spawn_timer += 1
    enemy_types = ['normal', 'fast', 'strong']
    
    if enemy_spawn_timer >= 50:
        random_enemy_type = random.choice(enemy_types)
        
        enemies.append(director.construct_enemy(builder, random_enemy_type))
        enemy_spawn_timer = 0
    
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()

pygame.quit()