import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 75
        self.top = 100
        self.cell_size = 30

    def set_view(self, left=None, top=None, cell_size=None):
        self.left = left or self.left
        self.top = top or self.top
        self.cell_size = cell_size or self.cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen,
                                 'white',
                                 (self.left + x * self.cell_size,
                                  self.top + y * self.cell_size,
                                  self.cell_size,
                                  self.cell_size),
                                 width=1
                                 )


if __name__ == '__main__':
    board = Board(10, 20)
    screen = pygame.display.set_mode((600, 800))
    running = True
    screen.fill('black')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board.render(screen)
        pygame.display.flip()
