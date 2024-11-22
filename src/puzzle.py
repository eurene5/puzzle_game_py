import pygame
import random

class Puzzle:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tiles = list(range(1, rows * cols)) + [0]
        random.shuffle(self.tiles)
        self.empty_tile = self.tiles.index(0)

    def draw(self, screen):
        tile_size = 600 // self.rows
        for row in range(self.rows):
            for col in range(self.cols):
                value = self.tiles[row * self.cols + col]
                if value != 0:
                    pygame.draw.rect(screen, (0, 0, 255),
                                     (col * tile_size, row * tile_size, tile_size, tile_size))
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(value), True, (255, 255, 255))
                    screen.blit(text, (col * tile_size + tile_size // 4, row * tile_size + tile_size // 4))

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
