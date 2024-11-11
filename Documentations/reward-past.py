# This class implements a reward function for a self-driving car
# It looks at the current speed and the previous speed to make a decision
# If the speed is greater than the previous speed, it adds 10 to the reward
# This incentivizes the car to go faster and faster
# This method of rewarding is based on past decisions
class Reward:
    def __init__(self, verbose=False, track_time=False):
        self.prev_speed = 0
        
    def reward_fun(self, params):
        speed = params['speed']
        reward = 0
        if (speed > self.prev_speed) and (self.prev_speed > 0):
            reward += 10
        self.prev_speed = speed  # update the previous speed
        return reward  # return the calculated reward

reward_obj = Reward()

def reward_function(params):
    reward = reward_obj.reward_fun(params)
    return float(reward)
