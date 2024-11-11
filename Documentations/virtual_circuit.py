class PARAMS:
    prev_speed = None
    prev_steering_angle = None 
    prev_steps = None
    prev_direction_diff = None
    prev_normalized_distance_from_route = None
def reward_function(params):
    
    # Read input parameters
    heading = params['heading']
    distance_from_center = params['distance_from_center']
    steps = params['steps']
    steering_angle = params['steering_angle']
    speed = params['speed']
# Reinitialize previous parameters if it is a new episode
    if PARAMS.prev_steps is None or steps < PARAMS.prev_steps:
        PARAMS.prev_speed = None
        PARAMS.prev_steering_angle = None
        PARAMS.prev_direction_diff = None
        PARAMS.prev_normalized_distance_from_route = None
    #Check if the speed has dropped
    has_speed_dropped = False
    if PARAMS.prev_speed is not None:
        if PARAMS.prev_speed > speed:
            has_speed_dropped = True
    #Penalize slowing down without good reason on straight portions
    if has_speed_dropped and not is_turn_upcoming: 
        speed_maintain_bonus = min( speed / PARAMS.prev_speed, 1 )
    #Penalize making the heading direction worse
    heading_decrease_bonus = 0
    if PARAMS.prev_direction_diff is not None:
        if is_heading_in_right_direction:
            if abs( PARAMS.prev_direction_diff / direction_diff ) > 1:
                heading_decrease_bonus = min(10, abs( PARAMS.prev_direction_diff / direction_diff ))
    #has the steering angle changed
    has_steering_angle_changed = False
    if PARAMS.prev_steering_angle is not None:
        if not(math.isclose(PARAMS.prev_steering_angle,steering_angle)):
            has_steering_angle_changed = True
    steering_angle_maintain_bonus = 1 
    #Not changing the steering angle is a good thing if heading in the right direction
    if is_heading_in_right_direction and not has_steering_angle_changed:
        if abs(direction_diff) < 10:
            steering_angle_maintain_bonus *= 2
        if abs(direction_diff) < 5:
            steering_angle_maintain_bonus *= 2
        if PARAMS.prev_direction_diff is not None and abs(PARAMS.prev_direction_diff) > abs(direction_diff):
            steering_angle_maintain_bonus *= 2
    #Reward reducing distance to the race line
    distance_reduction_bonus = 1
    if PARAMS.prev_normalized_distance_from_route is not None and PARAMS.prev_normalized_distance_from_route > normalized_distance_from_route:
        if abs(normalized_distance_from_route) > 0:
            distance_reduction_bonus = min( abs( PARAMS.prev_normalized_distance_from_route / normalized_distance_from_route ), 2)
    # Before returning reward, update the variables
    PARAMS.prev_speed = speed
    PARAMS.prev_steering_angle = steering_angle
    PARAMS.prev_direction_diff = direction_diff
    PARAMS.prev_steps = steps
    PARAMS.prev_normalized_distance_from_route = normalized_distance_from_route
