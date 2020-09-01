from gym.envs.registration import register

register(
    id='FourRooms-v0',
    entry_point='gridworlds.envs:FourRooms',
    
)  
register(
    id='FourRooms-v1',
    entry_point='gridworlds.envs:FourRoomsIntra',
    
)    

