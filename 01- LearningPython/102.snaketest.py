import random
import numpy as np  # Importa a biblioteca NumPy, frequentemente usada para computação numérica.

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700


class SnakeAgent:
    def __init__(self):
        self.state = None  # Inicializa o estado do agente como None.
        self.action = None  # Inicializa a ação do agente como None.
        self.action_probs = [0, 0, 0, 0]

        # Inicializa a função de política com uma distribuição uniforme.
        self.policy = np.ones(4) / 4

        # Cria a tabela Q.
        self.q_table = np.zeros((WINDOW_HEIGHT, WINDOW_WIDTH, 4))

    def perceive(self, game_state):
        self.state = game_state  # Define o estado do agente com base no estado do jogo recebido.

    def take_action(self):
        # Prever a ação que o agente deve tomar com base no estado atual do jogo.
        action_probs = self.policy(self.state)  # Chama a função de política para obter probabilidades de ação.
        self.action = np.random.choice(len(action_probs),
                                       p=action_probs)  # Escolhe uma ação aleatória com base nas probabilidades.

        return self.action

    def update_q_table(self, reward, new_state, new_action):
        # Atualiza a tabela Q.
        self.q_table[self.state][self.action] += self.learning_rate * (
            reward + self.discount_factor * np.max(self.q_table[new_state]) - self.q_table[self.state][self.action]
        )

    def learn(self):
        # Aprende a jogar o jogo.
        for _ in range(self.training_iterations):
            # O agente percebe o ambiente.
            self.perceive(game_state)

            # O agente toma uma ação.
            action = self.take_action()

            # O jogo é atualizado com a ação do agente.
            new_state, done = update_game_state(game_state, action)

            # O agente recebe uma recompensa.
            reward = get_reward(new_state)

            # O agente atualiza a tabela Q.
            self.update_q_table(reward, new_state, new_action)

            # Se o jogo acabou, pare o loop.
            if done:
                break

