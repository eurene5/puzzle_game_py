import pygame
from puzzle import Puzzle

class Game:
    def __init__(self, rows, cols, k=0):
        if rows < 2 or cols < 2:
            raise ValueError("Les dimensions du puzzle doivent être au moins 2x2.")
        self.rows = rows
        self.cols = cols
        self.k = k
        self.moves = 0
        self.running = True
        self.puzzle = Puzzle(rows, cols)

        self.screen = pygame.display.set_mode((600, 600))
        self.font = pygame.font.Font(None, 36)
        pygame.display.set_caption(f"{rows * cols - 1}-puzzle {k}-swap")

    def display_message(self, message):
        """Affiche un message au centre de l'écran."""
        self.screen.fill((255, 255, 255))
        text = self.font.render(message, True, (0, 255, 0))
        text_rect = text.get_rect(center=(300, 300))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)  # Attend 3 secondes avant de continuer

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            self.screen.fill((255, 255, 255))
            self.puzzle.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.puzzle.move("up")
                        self.moves += 1
                    elif event.key == pygame.K_DOWN:
                        self.puzzle.move("down")
                        self.moves += 1
                    elif event.key == pygame.K_LEFT:
                        self.puzzle.move("left")
                        self.moves += 1
                    elif event.key == pygame.K_RIGHT:
                        self.puzzle.move("right")
                        self.moves += 1

                    if self.k > 0 and self.moves % self.k == 0:
                        self.puzzle.swap()
                        print(f"Échange automatique des tuiles après {self.k} mouvements!")

                    if self.puzzle.is_solved():
                        self.display_message("Félicitations, vous avez résolu le puzzle!")
                        self.running = False

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
