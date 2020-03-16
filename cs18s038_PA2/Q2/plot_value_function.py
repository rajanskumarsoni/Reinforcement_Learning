import click
import numpy as np
import gym
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set()

from rlpa2 import chakra
env = gym.make('chakra-v0')
rng = np.random.RandomState(1)
gamma = .9
def include_bias(ob):
	p = ob.tolist()
	g =list(p)
	g.append(1)
	return g


def get_action(theta, state, rng=np.random):
	ob_1 = include_bias(state)
	mean = theta.dot(ob_1)
	r = rng.normal(loc=mean,scale=1.)
	return r


def find_vale(env, state, gamma):
	value = 0
	for i in range(100):
		decision = False
		rewards = []
		while decision == False :
			action = get_action(theta, state, rng=rng)
			state, reward, decision, _ = step(action,state)
			#print(reward)
			rewards.append(reward)
		returns = 0

		for j in np.sort(range(len(rewards)))[::-1]:

			returns = rewards[j] + gamma*returns
		#print(returns)
		value += returns
	return value/100



def step(action, state):
        #Fill your code here
        #print("action", action)

        m = np.max(np.abs(list(action)))
        action_x = action[0]/(40*m)
        action_y= action[1]/(40*m)
        if (-0.05 <= (state[0] + action_x) <= .05) and (-0.05 <= (state[1] + action_x) <= .05) :
            next_state = ((state[0] + action_x),(state[1] + action_y))
            state = next_state
          
            return np.array(state), 0,True, {}


       
        #print("action_x",action_x,"action_y",action_y)

        elif ((state[0] + action_x) <= 1) and ((state[0] + action_x) >= -1) and ((state[1] + action_y) <= 1) and ((state[1] + action_y) >= -1) :
            next_state = ((state[0] + action_x),(state[1] + action_y))
            reward = -(0.5*(state[0] + action_x)**2 + 10*0.5*(state[1] + action_y )**2)
            #reward = -np.sqrt((state[0] + action_x)**2 + (state[1] + action_y )**2)
            state = next_state
            # sprint("reward", reward)
            # print("kumar")
            return np.array(state), reward,False, {}

            
        else:
            reward = -1000

            #print("reweffeard", reward)
            # print("soni")
            return np.array(state), reward,True, {} # Return the next state and the reward, along with 2 additional quantities : False, {}
        



theta = np.load('theta.npy')

x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)
value_matrix = []
for i in x :
	value_array = []
	for j in y:
		z = find_vale(env, np.array([i,j]), gamma)
		value_array.append(z)
	value_matrix.append(value_array)


print(value_matrix)
# plt.imshow(np.array(value_matrix).T, cmap='hot', interpolation='nearest')
# plt.show()

uniform_data = np.array(value_matrix).T
ax = sns.heatmap(uniform_data)
plt.show()
