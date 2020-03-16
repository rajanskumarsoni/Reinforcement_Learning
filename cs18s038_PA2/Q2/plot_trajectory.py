import click
import numpy as np
import gym
import matplotlib.pyplot as plt

from rlpa2 import chakra
env = gym.make('chakra-v0')



def include_bias(ob):
	p = ob.tolist()
	g =list(p)
	g.append(1)
	return g


def chakra_get_action(theta, state, rng=np.random):
	ob_1 = include_bias(state)
	mean = theta.dot(ob_1)
	r = rng.normal(loc=mean,scale=1.)
	return mean



def test(env):
	get_action = chakra_get_action
	theta = np.load('theta.npy')
	
	for i in range(500):

		start_state  = env.reset()
		action = chakra_get_action(theta, start_state, rng = np.random)
		decision =  False
		
		trajectory = []
		trajectory.append(start_state)
		while not decision:
			next_state, reward, decision, _ = env.step(action)
			# print(next_state)
			action = chakra_get_action(theta, next_state, rng = np.random)
			#env.render()

			trajectory.append(next_state)

		trajectory = np.array(trajectory)
		
		
		# print("raj",len(trajectory[:,1]))
		# print("son",len(trajectory[:,0]))
		plt.plot(trajectory[:,1], trajectory[:,0])
	plt.title("trajectory")
	plt.show()
test(env)
