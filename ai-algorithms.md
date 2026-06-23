# AI Algorithms

Plan for AI algorithms to use for training on the Snake game.

| # | Algorithm | Type | Action Space | Reinforcement Learning | On/Off-Policy | Complexity |
|---|---|---|---|---|---|---|
| 1 | Q-Learning | Tabular RL | Discrete | ✓ | Off-policy | ⭐ |
| 2 | DQN | Deep RL | Discrete | ✓ | Off-policy | ⭐⭐ |
| 3 | NEAT | Evolutionary | Both | ✗ | — | ⭐⭐ |
| 4 | A2C | Actor-Critic | Both | ✓ | On-policy | ⭐⭐⭐ |
| 5 | PPO | Policy Gradient | Both | ✓ | On-policy | ⭐⭐⭐ |
| 6 | SAC | Actor-Critic | Continuous* | ✓ | Off-policy | ⭐⭐⭐⭐ |
| 7 | MCTS | Planning | Discrete | ✓ | — | ⭐⭐⭐⭐ |

## 1. Q-Learning

The agent keeps a lookup table where every row is a state and every column is an action. After each step it updates the cell using the Bellman equation: current reward plus discounted best future reward. Simple and guaranteed to converge in finite state spaces.

*For Snake: the table explodes in size as the body grows — you'll need a simplified state (e.g. relative food direction + 3 danger sensors) to keep it tractable. That limitation is the lesson.*

## 2. DQN

A neural network replaces the Q-table, approximating Q-values for any state without enumerating them. A replay buffer stores past transitions for reuse, and a frozen target network keeps training targets stable. The breakthrough that made deep RL practical.

*For Snake: the go-to first deep RL algorithm. Handles the full grid state comfortably and reuses past experience efficiently via the replay buffer.*

## 3. NEAT

Evolves a population of neural networks using genetic operators — mutation, crossover, and speciation. No gradients, no reward loop; fitness is all that matters. Speciation protects structural innovations long enough to prove themselves. Completely orthogonal to gradient-based methods.

*For Snake: each network plays a full game and is scored by length reached. No training loop — just selection pressure across generations. A useful contrast to everything else on this list.*

## 4. A2C

Two networks train together: the actor outputs a policy (what to do), the critic estimates state value (how good things are). The critic's estimate reduces variance in the actor's gradient updates, making training far more stable than pure policy gradient. A2C is synchronous; A3C runs multiple workers in parallel.

*For Snake: a natural stepping stone before PPO. Stable enough to learn the full game without a simplified state.*

## 5. PPO

Extends actor-critic with a clipped surrogate objective that prevents the policy from changing too drastically in a single update. Achieves the stability of TRPO without expensive second-order optimisation. The dominant general-purpose RL algorithm today.

*For Snake: likely your best final agent. Stable training, tolerates long episodes as the snake grows, and scales well without much hyperparameter tuning.*

## 6. SAC

An off-policy actor-critic that maximises both reward and policy entropy simultaneously. The entropy bonus drives automatic exploration and prevents premature convergence. Highly sample efficient due to off-policy learning. Natively continuous but a discrete variant exists.

*For Snake: use Discrete SAC. More sample efficient than PPO and more modern — good choice if you want to push performance beyond PPO.*

## 7. MCTS

A planning algorithm that builds a search tree at decision time by simulating future states. Balances exploration and exploitation using the UCB formula. Requires a perfect environment model to simulate against. No learning between games — it plans fresh each move. Foundation of AlphaZero.

*For Snake: you already have a perfect model — the game itself. No training needed; the agent just thinks ahead. Architecturally unlike everything else on this list.*