from gym import Env
from gym.envs.registration import register
from gym.utils import seeding
from gym import spaces
import numpy as np


class chakra(Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 50
    }

    def __init__(self):
        self.action_space = spaces.Box(low=-1, high=1, shape=(2,))
        self.observation_space = spaces.Box(low=-1, high=1, shape=(2,))

        self._seed()
        self.viewer = None
        self.state = None

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self,action):
        #Fill your code here
        #print("action", action)

        m = np.max(np.abs(list(action)))
        action_x = action[0]/(40*m)
        action_y= action[1]/(40*m)
        if (-0.05 <= (self.state[0] + action_x) <= .05) and (-0.05 <= (self.state[1] + action_x) <= .05) :
            next_state = ((self.state[0] + action_x),(self.state[1] + action_y))
            self.state = next_state
            print("Rajan son")
            return np.array(self.state), 0,True, {}


       
        #print("action_x",action_x,"action_y",action_y)

        elif ((self.state[0] + action_x) <= 1) and ((self.state[0] + action_x) >= -1) and ((self.state[1] + action_y) <= 1) and ((self.state[1] + action_y) >= -1) :
            next_state = ((self.state[0] + action_x),(self.state[1] + action_y))
            # reward = -(0.5*(self.state[0] + action_x)**2 + 10*0.5*(self.state[1] + action_y )**2)
            reward = 2-np.sqrt((self.state[0] + action_x)**2 + (self.state[1] + action_y )**2)
            self.state = next_state
            # sprint("reward", reward)
            # print("kumar")
            return np.array(self.state), reward,False, {}

            
        else:
            reward = -200

            #print("reweffeard", reward)
            # print("soni")
            return np.array(self.state), reward,True, {} # Return the next state and the reward, along with 2 additional quantities : False, {}
        

    def _reset(self):
        while True:
            self.state = self.np_random.uniform(low=-1, high=1, size=(2,))
            # Sample states that are far away
            if np.linalg.norm(self.state) > 0.9:
                break
        
        # return np.array(self.state)
        return np.array(self.state)

    # method for rendering

    def _render(self, mode='human', close=False):
        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return

        screen_width = 800
        screen_height = 800

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)

            agent = rendering.make_circle(
                min(screen_height, screen_width) * 0.03)
            origin = rendering.make_circle(
                min(screen_height, screen_width) * 0.03)
            trans = rendering.Transform(translation=(0, 0))
            agent.add_attr(trans)
            self.trans = trans
            agent.set_color(1, 0, 0)
            origin.set_color(0, 0, 0)
            origin.add_attr(rendering.Transform(
                translation=(screen_width // 2, screen_height // 2)))
            self.viewer.add_geom(agent)
            self.viewer.add_geom(origin)

        # self.trans.set_translation(0, 0)
        self.trans.set_translation(
            (self.state[0] + 1) / 2 * screen_width,
            (self.state[1] + 1) / 2 * screen_height,
        )

        return self.viewer.render(return_rgb_array=mode == 'rgb_array')


register(
    'chakra-v0',
    entry_point='rlpa2.chakra:chakra',
    timestep_limit=10000,
)
