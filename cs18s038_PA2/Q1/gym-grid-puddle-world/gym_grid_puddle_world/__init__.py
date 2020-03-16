from gym.envs.registration import register

register(
    id='puddleworld-v0',
    entry_point='gym_grid_puddle_world.envs:Puddle_world_Env',
)