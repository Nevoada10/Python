import gym
import tensorflow as tf
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import median, mean
from collections import Counter


LR = 1e-3  # Learning rate for neural network
env = gym.make("CartPole-v0")  # Create the CartPole environment
env.reset()  # Reset the environment to its initial state
goal_steps = 500  # Number of steps an episode should run to be considered successful
score_requirement = 50  # Minimum average score required to train the model
initial_games = 10000  # Number of games to play for collecting training data


def some_random_games_first():
    for episode in range(5):  # Play 5 episodes of the game
        env.reset()  # Reset the environment for a new episode
        for t in range(200):  # Each episode can run up to 200 steps
            env.render()  # Render the environment (visualization, optional but slower)

            action = env.action_space.sample()  # Choose a random action (0 or 1)
            observation, reward, done, info = env.step(action)  # Take the chosen action

            if done:  # If the episode is over (pole fell), exit the loop
                break
