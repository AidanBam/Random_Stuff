class Block:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.color = (245, 215, 135) if value == 4 else (133, 121, 121)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, 80, 80))

def spawn_block(blocks):
    new_block_value = 4 if random.randint(1, 10) == 4 else 2
    empty_positions = [(x, y) for x in range(440, 800, 90) for y in range(160, 520, 90) if (x, y) not in [(block.x, block.y) for block in blocks]]
    if empty_positions:
        x, y = random.choice(empty_positions)
        blocks.append(Block(x, y, new_block_value))