import random
import numpy as np

# Define the Minesweeper environment
class MinesweeperEnv:
    def __init__(self, size=5, num_mines=5):
        self.size = size
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.generate_mines()

    def get_state(self, row, col):
        if not self.is_valid(row, col):
            return -1  # Invalid state
        elif self.board[row][col] == ' ':
            return 0  # Unrevealed cell
        elif self.board[row][col] == '*':
            return -1  # Mine
        else:
            return int(self.board[row][col])  # Number of adjacent mines

    def generate_mines(self):
        positions = random.sample(range(self.size * self.size), self.num_mines)
        for pos in positions:
            row = pos // self.size
            col = pos % self.size
            self.board[row][col] = '*'

    def display(self):
        for row in self.board:
            print(' '.join(row))

    def is_mine(self, row, col):
        return self.board[row][col] == '*'

    def is_valid(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def count_adjacent_mines(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if self.is_valid(r, c) and self.is_mine(r, c):
                    count += 1
        return count

    def get_state(self, row, col):
        if not self.is_valid(row, col):
            return -1  # Invalid state
        elif self.board[row][col] == ' ':
            return 0  # Unrevealed cell
        elif self.board[row][col] == '*':
            return -10  # Mine
        else:
            return int(self.board[row][col])  # Number of adjacent mines

    def step(self, action):
        row, col = action
        if self.is_mine(row, col):
            return self.get_state(row, col), -10, True
        else:
            return self.get_state(row, col), 0, False

# Define the Q-learning agent
class QLearningAgent:
    def __init__(self, env, alpha=1000000000000000000000, gamma=1, epsilon=10000000000000000000000000):
        self.env = env
        self.q_table = np.zeros((env.size, env.size))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def update_q_table( self, state, action, reward, next_state ):
        row, col = action
        if next_state == -10:  # If the next state is a mine
            self.q_table[ row ][ col ] = reward  # Update Q-value for mine state
        else:
            next_row, next_col = np.unravel_index( next_state, self.q_table.shape )
            self.q_table[ row ][ col ] += self.alpha * (
                        reward + self.gamma * np.max( self.q_table[ next_row, next_col ] ) - self.q_table[ row ][ col ])

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice([(i, j) for i in range(self.env.size) for j in range(self.env.size)])
        else:
            return np.unravel_index(np.argmax(self.q_table, axis=None), self.q_table.shape)

    def update_q_table( self, state, action, reward, next_state ):
        row, col = action
        if next_state == -10:  # If the next state is a mine
            self.q_table[ row ][ col ] = reward  # Update Q-value for mine state
        else:
            self.q_table[ row ][ col ] += self.alpha * (reward + self.gamma * np.max( self.q_table[ next_state ] ) - self.q_table[ row ][ col ])


# Training loop
env = MinesweeperEnv()
agent = QLearningAgent(env)

num_episodes = 10000000000000
for episode in range(num_episodes):
    total_reward = 0

    # Generate random starting position for each episode
    row, col = random.randint(0, env.size - 1), random.randint(0, env.size - 1)

    while True:
        state = env.get_state(row, col)
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.update_q_table(state, action, reward, next_state)
        total_reward += reward
        if done:
            break

        # If the next state is a mine, generate a new starting position
        if next_state == -10:
            row, col = random.randint(0, env.size - 1), random.randint(0, env.size - 1)

print("Q-table after training:")
print(agent.q_table)
