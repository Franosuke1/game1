import pygame

my_list = [1, 2, 3]  # список
my_tuple = (1, 2, 3)  # кортеж

main_screen = pygame.display.set_mode((500, 300))
main_screen.fill((0, 0, 125))

actor_interface_surf = pygame.surface.Surface((50, 50))
actor_interface_surf.fill((200, 0, 0))

actor_base_rect = pygame.Rect(100, 100, 50, 100)
actor_rect = pygame.draw.rect(main_screen, (255, 255, 255), actor_base_rect)

skill_1_rect = pygame.Rect(50, 250, 25, 25)
skill_1_button = pygame.draw.rect(main_screen, (150, 0, 255), skill_1_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if actor_rect.collidepoint(event.pos):
                main_screen.blit(actor_interface_surf, (0, 0))

            elif skill_1_button.collidepoint(event.pos):
                print('Fire!')

    pygame.display.update()




