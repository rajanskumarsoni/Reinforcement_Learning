import numpy as np
import matplotlib.image as mpimg 
from matplotlib import pyplot as plt
import gym
from gym import error, spaces, utils
from gym.utils import seeding

""" Four rooms. The goal is either in the 3rd room, or in a hallway adjacent to it
"""

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
R0OPTION0 = 4
R0OPTION1 = 5
R1OPTION0 = 6
R1OPTION1 = 7
R2OPTION0 = 8
R2OPTION1 = 9
R3OPTION0 = 10
R3OPTION1 = 11

NUM_ROOMS = 4
# def constant(f):
#     def fset(self, value):
#         raise TypeError
#     def fget(self):
#         return f()
#     return property(fget, fset)

# class _Const(object):
#     @constant
#     def():
#         return  [ [2,5], [6,2], [2,-1], [-1,1] ]


class FourRooms(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self):

		self.room_sizes = [[5,5], [6,5], [4,5], [5,5]]
	    # all cooridinate are according to room 
		self.gamma = .9
		self.pre_hallways = [ 
			{ tuple([2,4]) : [RIGHT, 0], tuple([4,1]) : [DOWN, 3]},
			{ tuple([2,0]) : [LEFT, 0], tuple([5,2]) : [DOWN, 1]},
			{ tuple([0,2]) : [UP, 1], tuple([2,0]) : [LEFT, 2]},
			{ tuple([3,4]) : [RIGHT, 2], tuple([0,1]) : [UP, 3]},
			]
		 # each hallway is assigned to each room
		self.hallway_coords = [ [2,5], [6,2], [2,-1], [-1,1] ]
		# each row corressponds to one room and each row consist 4 outputs according  option selected
		self.hallways = [ #self.hallways[i][j] = [next_room, next_coord] when taking option j from hallway i#
			[ [0, self.hallway_coords[0]], [1, [2,0]], [0, self.hallway_coords[0]], [0, [2,4]] ],
			[ [1, [5,2]], [1, self.hallway_coords[1]], [2, [0,2]], [1, self.hallway_coords[1]] ],
			[ [2, self.hallway_coords[2]], [2, [2,0]], [2, self.hallway_coords[2]], [3, [3,4]] ],
			[ [0, [4,1]], [3, self.hallway_coords[3]], [3, [0,1]], [3, self.hallway_coords[3]] ]
			]
	    # options for room 0
	    
	    
		self.offsets = [0] * (NUM_ROOMS + 1)
		for i in range(NUM_ROOMS):
			self.offsets[i + 1] = self.offsets[i] + self.room_sizes[i][0] * self.room_sizes[i][1] + 1
		self.n_states = self.offsets[4] + 1
		self.absorbing_state = self.n_states

		self.goal_set = [[2, [1, 2]],[1,[6,2]]]
		self.option_set = [[0,1,2,3,4,5],[0,1,2,3,6,7],[0,1,2,3,8,9],[0,1,2,3,10,11]]
		self.hallway_option_set = [[0,1,2,3,4,7],[0,1,2,3,6,9],[0,1,2,3,8,11],[0,1,2,3,5,10]]

		self.noise = .33
		self.step_reward = 0.0
		self.terminal_reward = 1.0
		self.bump_reward = -0.1
		self.step_count = 1

	    # start state random location in start room
		# start_room = np.random.choice([0,1,2,3])
		# sz = self.room_sizes[start_room]
		# self.start_state = self.offsets[start_room] + np.random.randint(sz[0]*sz[1] - 1)
		self.reset()

		self.option_space = spaces.Discrete(12)
		self.observation_space = spaces.Discrete(self.n_states) # with absorbing state
	    
    # self._wfwefwef()
    # self._seed

	def room_options(self, option, room, coord, in_hallway) :
		# print("start", self.hallway_coords)
		step_count = 0
		# option for room 0
		if option == 4 :

			while(coord != self.hallway_coords[3]):
				step_count +=1
				if coord == [4,1] :
					coord = self.hallway_coords[3].copy()
				elif coord[1] == 1 :
					coord[0] +=1 
				elif coord[1] > 1 :
					coord[1] -=1
				elif coord[1] < 1 :
					coord[1] +=1
			return step_count , [3, self.hallway_coords[3].copy()]
		elif option == 5:
			if room == 3 :
				coord = [4,1]
				step_count +=1

			while(coord != self.hallway_coords[0]):
				# print("kumar")
				step_count +=1
				if coord[0] == 2 :
					coord[1] +=1 
				elif coord[0] > 2 :
					coord[0] -=1
				elif coord[0] < 2 :
					coord[0] +=1
			return step_count , [0, self.hallway_coords[0].copy()]
		# options for room 1
		elif option == 6 :
			while(coord != self.hallway_coords[0]):
				step_count +=1
				if coord == [2,0] :
					coord = self.hallway_coords[0].copy()
				elif coord[0] == 2 :
					coord[1] -=1 
				elif coord[0] > 2 :
					coord[0] -=1
				elif coord[0] < 2 :
					coord[0] +=1
			return step_count , [0, self.hallway_coords[0].copy()]
		elif option == 7:
			if room == 0 :
				coord =  [2,0]
				step_count +=1
			while(coord != self.hallway_coords[1]):
				# print(self.hallway_coords)
				# print("self.hallway_coords[1]",self.hallway_coords[1])
				# print("soni",coord)
				step_count +=1
				if coord[1] == 2 :
					coord[0] +=1 
				elif coord[1] > 2 :
					coord[1] -=1
				elif coord[1] < 2 :
					coord[1] +=1
			return step_count , [1, self.hallway_coords[1].copy()]
		# options for room 2
		elif option == 8 :
			while(coord != self.hallway_coords[1]):
				step_count +=1
				if coord == [0,2] :
					coord = self.hallway_coords[1].copy()
				elif coord[1] == 2 :
					coord[0] -=1 
				elif coord[1] > 2 :
					coord[1] -=1
				elif coord[1] < 2 :
					coord[1] +=1
			return step_count , [ 1, self.hallway_coords[1].copy()]
		elif option == 9:
			if room == 1 :
				coord = [0,2]
				step_count +=1
			while(coord != self.hallway_coords[2]):
				step_count +=1
				if coord[0] == 2 :
					coord[1] -=1 
				elif coord[0] > 2 :
					coord[0] -=1
				elif coord[0] < 2 :
					coord[0] +=1
			return step_count , [ 2, self.hallway_coords[2]]
		# options for room 3
		elif option == 10 :
			# print("10", self.hallway_coords[2] )
			while(coord != self.hallway_coords[2]):
				step_count +=1
				if coord == [3,4] :
					coord = self.hallway_coords[2].copy()
				elif coord[0] == 3 :
					coord[1] +=1 
				elif coord[0] > 3 :
					coord[0] -=1
				elif coord[0] < 3 :
					coord[0] +=1
			return step_count , [ 2, self.hallway_coords[2].copy()]
		elif option == 11:
			if room == 2 :
				coord = [3,4]
				step_count +=1
			while(coord != self.hallway_coords[3]):
				# print("rajan", coord)
				step_count +=1
				if coord[1] == 1 :
					coord[0] -=1 
				elif coord[1] > 1:
					coord[1] -=1
				elif coord[1] < 1 :
					coord[1] +=1
			return step_count , [ 3, self.hallway_coords[3].copy()]


	def ind2coord(self, index, sizes=None):
		if sizes is None:
			sizes = [self.n]*2
		[rows, cols] = sizes

		assert(index >= 0)

		row = index // cols
		col = index % cols

		return [row, col]


	def coord2ind(self, coord, sizes=None):
		if sizes is None:
			sizes = [self.n]*2

		[rows, cols] = sizes
		[row, col] = coord

		assert(row < rows)
		assert(col < cols)

		return row * cols + col
    # it return whether index is in hallway or not
	def in_hallway_index(self, index=None):
		if index is None:
			index = self.state
		return index in [offset - 1 for offset in self.offsets]

	def in_hallway_coord(self, coord):
		# print("1", self.hallway_coords)
		return coord in self.hallway_coords

	def encode(self, location, in_hallway=None): 
		[room, coord] = location
		if in_hallway is None:
			in_hallway = self.in_hallway_coord(coord)

		if in_hallway:
			return self.offsets[room + 1] - 1
		  # maybe have hallways as input
		ind_in_room = self.coord2ind(coord, sizes=self.room_sizes[room])
		return ind_in_room + self.offsets[room]

	def decode(self, index, in_hallway=None):
		if in_hallway is None:
			in_hallway = self.in_hallway_index(index=index)

		room = [r for r, offset in enumerate(self.offsets[1:5]) if index < offset][0]
		if in_hallway:
			# print("2", self.hallway_coords)
			coord_in_room = self.hallway_coords[room].copy()
		else:
			coord_in_room = self.ind2coord(index - self.offsets[room], sizes=self.room_sizes[room])
		return room, coord_in_room # hallway

	def step(self, option):
		assert self.option_space.contains(option)

		if self.state == self.terminal_state:

			self.state = self.absorbing_state
			self.done = True
			return self.state, self.get_reward(), self.done, None

		in_hallway = self.in_hallway_index()
		# print("in_hallway", in_hallway)
		[room, coord]= self.decode(self.state, in_hallway=in_hallway)
		room2 = room; coord2 = coord

		if np.random.rand() < self.noise:
			if in_hallway :
				option = np.random.choice(self.hallway_option_set[room])
			else :
				option = np.random.choice(self.option_set[room])
		# print("step_inside_opttion", option)

		if in_hallway: # hallway option
			if option <4 :
				[room2, coord2] = self.hallways[room][option]
			else :
				step_count , [room2, coord2] = self.room_options(option,room, coord, in_hallway)


		elif tuple(coord) in self.pre_hallways[room].keys():
			if option <4 :

				hallway_info = self.pre_hallways[room][tuple(coord)]
				if option == hallway_info[0]:
					room2 = hallway_info[1]
					# print("3", self.hallway_coords)
					coord2 = self.hallway_coords[room2].copy()
				else :
					[row, col] = coord
					[rows, cols] = self.room_sizes[room]
					if option == UP:
						row = max(row - 1, 0)
					elif option == DOWN:
						row = min(row + 1, rows - 1)
					elif option == RIGHT:
						col = min(col + 1, cols - 1)
					elif option == LEFT:
						col = max(col - 1, 0)
					coord2 = [row, col]
			else :
				step_count , [room2, coord2] = self.room_options(option,room, coord, in_hallway = False)

	    
	    
		else: # normal option
			if option <4:
				[row, col] = coord
				[rows, cols] = self.room_sizes[room]
				if option == UP:
					row = max(row - 1, 0)
				elif option == DOWN:
					row = min(row + 1, rows - 1)
				elif option == RIGHT:
					col = min(col + 1, cols - 1)
				elif option == LEFT:
					col = max(col - 1, 0)
				coord2 = [row, col]
			else :
				step_count , [room2, coord2] = self.room_options(option, room, coord, in_hallway= False)






		new_state = self.encode([room2, coord2])
		
		if option < 4 :
			self.step_count = 1
			reward = self.get_reward(new_state=new_state)
		else :
			# print("self.step_count ",self.step_count )
			self.step_count = step_count
			reward = 0*self.gamma**(self.step_count-1)
		self.state = new_state
		return new_state, reward, self.done, None




	def get_reward(self, new_state=None):
		if self.done:
			return self.terminal_reward

		reward = self.step_reward

		if self.bump_reward != 0 and self.state == new_state:
			reward = self.bump_reward

		return reward

	def at_border(self):
		[row, col] = self.ind2coord(self.state)
		return (row == 0 or row == self.n - 1 or col == 0 or col == self.n - 1)


	def reset(self):
		self.state = np.random.randint(self.n_states - 1)
		self.done = False
		self.state = self.encode([3,[2,2]])
		return self.state

	def set_goal(self,ind ) :
		self.terminal_state = self.encode(self.goal_set[ind])



	def render(self, mode='human', close=False):
		img = mpimg.imread('a.png') 
		f, axarr = plt.subplots(2,2)
		axarr[0,0].imshow(img, interpolation='nearest')
		axarr[0,0].axis('off')
		axarr[0,1].imshow(img, interpolation='nearest')
		axarr[0,1].axis('off')
		axarr[1,0].imshow(img, interpolation='nearest')
		axarr[1,0].axis('off')
		axarr[1,1].imshow(img, interpolation='nearest')
		axarr[1,1].axis('off')
		plt.axis('off')
		plt.subplots_adjust(wspace=0, hspace=0, left=0, right=1, bottom=0, top=1)
		plt.show()
      
