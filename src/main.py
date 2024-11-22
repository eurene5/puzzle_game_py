import pygame
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Puzzle Game")
    font = pygame.font.Font(None, 36)

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((255, 255, 255))
        title = font.render("Puzzle Game - Choose Mode", True, (0, 0, 0))
        screen.blit(title, (150, 50))

        instructions = [
            "Use the arrow keys to move tiles.",
            "Press 1 for 8-puzzle mode.",
            "Press 2 for 15-puzzle mode."
        ]
        for i, line in enumerate(instructions):
            text = font.render(line, True, (0, 0, 0))
            screen.blit(text, (20, 300 + i * 30))

        modes = ["8-puzzle", "15-puzzle"]
        for i, mode in enumerate(modes):
            text = font.render(f"{i + 1}. {mode}", True, (0, 0, 255))
            screen.blit(text, (150, 150 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game = Game(3, 3)  # 8-puzzle
                    game.run()
                elif event.key == pygame.K_2:
                    game = Game(4, 4)  # 15-puzzle
                    game.run()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
