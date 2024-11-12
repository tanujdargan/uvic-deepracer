class Reward:
    def __init__(self, verbose=False, track_time=False):
        self.prev_steering_angle = 0
        
    def reward_funciton(self, params):
    prev_steering_angle = self.prev_steering_angle
    steering_angle = params['steering_angle']
    self.prev_steering_angle = steering_angle
    steering_diff = abs(steering_angle - prev_steering_angle)
    reward_steering_smoothness = math.exp(-0.5 * steering_diff)

    #... Perform other functionalities
    #... return weighted reward

reward_obj = Reward()

def reward_function(params):
    reward = reward_obj.reward_fun(params)
    return float(reward)


