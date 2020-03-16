import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
class Puddle_world_Env(gym.Env):
    metadata = {'render.modes': ['human']}
    
    
    
    def __init__(self):

        # Initialize the grid world
        self.grid_world = np.zeros([12,12], dtype=np.int64)
        

        # self.start_positions = [[6,0],[7,0],[10,0],[11,0]]

        # Goal positions A, B, C
        self.grid_goals = [[0,11],[2,9],[6,7]]

        # Allowed actions
        # Our origin is on the top left corner
        self.grid_actions = {0 : [-1,0], # North
                        1 : [0,1],  # East
                        2 : [0,-1], # West
                        3 : [1,0]   # South
                        } 

        # All actions
        self.action_space = spaces.Discrete(len(self.grid_actions))
        
        # All states
        self.observation_space = spaces.Box(low = -3, high = 10, shape = self.grid_world.shape)
        
        # print(self.action_space)
        # print(self.observation_space)

        # Set rewards for the puddle
        self.grid_world[2:9,3:9]      -= 1
        self.grid_world[3:8,4:8]      -=1
        self.grid_world[4:7,5:7]      -=1
        self.grid_world[5:7,6]        +=1
        self.grid_world[6:8,7]        +=1
        self.grid_world[7:9,8]        +=1

        # initilalize reward
        self.reward = 0

    # Return the the goal position and enables wind for goals : A, B and disable wind for goal : C
    # Also sets the reward at the goal position
    def setting_goal(self,goal):
        if goal=='A':
            x, y = self.grid_goals[0]
            self.grid_world[x,y] = 10
            self.wind = 1
            return self.grid_goals[0]
        elif goal=='B':
            x, y = self.grid_goals[1]
            self.grid_world[x,y] = 10
            self.wind = 1
            return self.grid_goals[1]
        elif goal=='C':
            x, y = self.grid_goals[2]
            self.grid_world[x,y] = 10
            self.wind = 0
            return self.grid_goals[2]

    
    # def get_state(self):
    #     return self.current_position

    # Returns the action after considering the stochastic nature of actions to take place 
    def actual_action_taken(self, selected_action):
        # Set the probabilities of performing an action 
        probs = [0.1/3, 0.1/3, 0.1/3, 0.1/3]
        probs[selected_action] = 0.9
        # Select an action according to probabilities        
        action_took = np.random.choice([0,1,2,3],1,p = probs) # if p = is not given, its not working
        action_took = action_took[0]

        return action_took


    def step(self, current_state, action):
        # Return the postion,reward after performing an action.

        # Select the action by considering stochastic nature after selecting an action
        resulted_action = self.actual_action_taken(action)


        if self.wind:
            # Westerly blowing, that will wind_shift you one additional cell to the east with probability of 0.5
            self.wind_shift = np.random.choice(range(2),1,[0.5,0.5])
            self.wind_shift = self.wind_shift[0]
        else:
            self.wind_shift = 0
        
        # According to the action taken, returns the reward and the next state
        if (current_state[0] + self.grid_actions[resulted_action][0] < 0 or
            current_state[0] + self.grid_actions[resulted_action][0] > 11 or
            current_state[1] + self.grid_actions[resulted_action][1] + self.wind_shift < 0 or
            current_state[1] + self.grid_actions[resulted_action][1] + self.wind_shift > 11)  :
            # Transitions that take you off the grid will not result in any change

            self.reward = self.grid_world[current_state[0],current_state[1]]
            next_state = current_state
            return next_state, self.reward


        else : 
            x = current_state[0] + self.grid_actions[resulted_action][0]
            y = current_state[1] + self.grid_actions[resulted_action][1] +self.wind_shift
            next_state = [x,y]
            self.reward = self.grid_world[next_state[0],next_state[1]]

            return next_state, self.reward


    # Picks a random action
    def take_random_action(self):
        self.action = np.random.choice([0,1,2,3])
        return self.action

    # Brings our agent back to one of the start state
    def reset(self):
        # select a random start state
        idx = np.random.choice([0,1,2,3])
        s_pos = [[5,0],[6,0],[10,0],[11,0]]

        self.pos = s_pos[idx]
        return self.pos
  
    

    def render(self, mode='human'):
        ...

    def close(self):
        ...
