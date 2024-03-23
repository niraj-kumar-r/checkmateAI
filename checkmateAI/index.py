
import random
from gym_chess import ChessEnvV2

env = ChessEnvV2()

# current state
state = env.state

# select a move and convert it into an action
moves = env.possible_moves
move = random.choice(moves)
print("MOVE", move)
action = env.move_to_action(move)

# # or select an action directly
# actions = env.possible_actions
# action = random.choice(actions)

# pass it to the env and get the next state
new_state, reward, done, info = env.step(action)

print(env.state["board"])
