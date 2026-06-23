"""
Q-Learning
#: 1
Type: Tabular RL
Action Space: Discrete
Reinforcement Learning: ✓
On/Off-Policy: Off-policy
Complexity: ⭐

Description: The agent keeps a lookup table where every row is a state
and every column is an action. After each step it updates the cell using
the Bellman equation: current reward plus discounted best future reward.
Simple and guaranteed to converge in finite state spaces.

For Snake: the table explodes in size as the body grows — you'll need a
simplified state (e.g. relative food direction + 3 danger sensors) to keep
it tractable. That limitation is the lesson.
"""

"""
NumPy:          A python library used for working with arrays
Matplotlib:     Helps plot and create visualizations of data
                pip install matplotlib ipython
Pytorch:        A machine learning framework that helps create neural networks
                pip install torch torchvison 

States (5)
Danger: 
    danger_straight, danger_right, danger_left	
    Will the snake collide if it moves in any direction?
Direction: 
    dir_left, dir_right, dir_up, dir_down
    Which direction is the snake heading?
Food: 
    food_left, food_right, food_up, food_down
    In which direction is the food?
"""
