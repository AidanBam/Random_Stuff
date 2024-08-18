import numpy as np

# Define the environment
class Environment:
    def __init__(self):
        self.state = 0  # Initial state
        self.target = np.random.randint(0, 10)  # Target number to reach

    def step(self, action):
        if action == 0:  # Decrease the state
            self.state = max(0, self.state - 1)  # Clip the state to stay within bounds
        elif action == 1:  # Increase the state
            self.state = min(9, self.state + 1)  # Clip the state to stay within bounds

        # Calculate reward based on the difference between the current state and the target
        reward = -abs(self.state - self.target)

        # Check if the target is reached
        done = self.state == self.target

        return self.state, reward, done

# Define the agent
class QLearningAgent:
    def __init__(self, num_states, num_actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = np.zeros((num_states, num_actions))

    def choose_action(self, state):
        # Epsilon-greedy policy
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.num_actions)  # Exploration
        else:
            return np.argmax(self.q_table[state, :])  # Exploitation

    def update_q_table(self, state, action, reward, next_state):
        # Q-learning update rule
        self.q_table[state, action] += self.learning_rate * (reward + self.discount_factor * np.max(self.q_table[next_state, :]) - self.q_table[state, action])

# Initialize the environment and the agent
env = Environment()
agent = QLearningAgent(num_states=10, num_actions=2)

# Training loop
num_episodes = 100000
for episode in range(num_episodes):
    state = env.state
    total_reward = 0

    while True:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.update_q_table(state, action, reward, next_state)
        total_reward += reward
        state = next_state

        if done:
            break

    if (episode + 1) % 100 == 0:
        print(f'Episode {episode + 1}/{num_episodes}, Total Reward: {total_reward}')

# Test the agent
state = env.state
while True:
    action = agent.choose_action(state)
    next_state, reward, done = env.step(action)
    print(f'State: {state}, Action: {action}, Reward: {reward}, Next State: {next_state}')
    state = next_state

    if done:
        print('Target reached!')
        break