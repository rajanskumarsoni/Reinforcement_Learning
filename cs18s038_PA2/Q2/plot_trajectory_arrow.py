import click
import numpy as np
import gym
import matplotlib.pyplot as plt

from matplotlib.pyplot import figure 

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
	x = np.arange(-1, 1, 0.1)
	y = np.arange(-1, 1, 0.1)

# a = np.array([3,5,9])
	xx, yy = np.meshgrid(x, y, sparse=True)
	plt.figure(num = 1, figsize=(1,1))
	axes = plt.gca()
	axes.set_xlim([-1,1])
	axes.set_ylim([-1,1])
	for i in x:
		for j in y:
			print(i,j)
			action = chakra_get_action(theta, np.array([i,j]), rng = np.random)
			m = np.max(np.abs(list(action)))
			action_x = action[0]/(40*m)
			action_y= action[1]/(40*m)
			plt.arrow(i, j, action_x, action_y,  width = .005, facecolor = 'green')
	
	plt.title("policy")
	plt.show()
test(env)
