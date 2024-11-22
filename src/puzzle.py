import pygame
import random

class Puzzle:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tiles = list(range(1, rows * cols)) + [0]
        while True:
            random.shuffle(self.tiles)
            self.empty_tile = self.tiles.index(0)
            if self.is_solvable():
                break

    def draw(self, screen):
        tile_size = 600 // self.rows
        for row in range(self.rows):
            for col in range(self.cols):
                value = self.tiles[row * self.cols + col]
                x, y = col * tile_size, row * tile_size
                if value != 0:
                    pygame.draw.rect(screen, (0, 0, 255), (x, y, tile_size, tile_size))
                    pygame.draw.rect(screen, (0, 0, 0), (x, y, tile_size, tile_size), 3)
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(value), True, (255, 255, 255))
                    text_rect = text.get_rect(center=(x + tile_size // 2, y + tile_size // 2))
                    screen.blit(text, text_rect)

    def move(self, direction):
        row, col = divmod(self.empty_tile, self.cols)
        if direction == "up" and row > 0:
            self.swap_tiles(row, col, row - 1, col)
        elif direction == "down" and row < self.rows - 1:
            self.swap_tiles(row, col, row + 1, col)
        elif direction == "left" and col > 0:
            self.swap_tiles(row, col, row, col - 1)
        elif direction == "right" and col < self.cols - 1:
            self.swap_tiles(row, col, row, col + 1)

    def swap_tiles(self, row1, col1, row2, col2):
        idx1 = row1 * self.cols + col1
        idx2 = row2 * self.cols + col2
        self.tiles[idx1], self.tiles[idx2] = self.tiles[idx2], self.tiles[idx1]
        self.empty_tile = idx2

    def swap(self):
        idx1, idx2 = random.sample(range(len(self.tiles) - 1), 2)
        self.tiles[idx1], self.tiles[idx2] = self.tiles[idx2], self.tiles[idx1]

    def is_solved(self):
        return self.tiles == list(range(1, self.rows * self.cols)) + [0]

    def is_solvable(self):
        inversions = 0
        for i in range(len(self.tiles)):
            for j in range(i + 1, len(self.tiles)):
                if self.tiles[i] != 0 and self.tiles[j] != 0 and self.tiles[i] > self.tiles[j]:
                    inversions += 1
        if self.rows % 2 == 1:  # Grille avec un nombre impair de lignes
            return inversions % 2 == 0
        else:  # Grille avec un nombre pair de lignes
            empty_row = self.empty_tile // self.cols
            return (inversions + self.rows - 1 - empty_row) % 2 == 0
