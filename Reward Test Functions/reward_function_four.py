import math
def reward_function(params):
    '''
    Advanced reward function that encourages:
    1. Staying on the optimal racing line (left side bias)
    2. Smooth acceleration through corners
    3. Appropriate speed based on steering angle
    4. Progressive steering adjustments
    '''
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']
    steering_angle = abs(params['steering_angle'])
    speed = params['speed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    
    # Initialize reward
    reward = 1.0
    
    # Parameters for optimal line
    left_offset_target = -0.3 * track_width
    marker_1 = abs(left_offset_target - 0.1 * track_width)
    marker_2 = abs(left_offset_target - 0.25 * track_width)
    marker_3 = abs(left_offset_target - 0.5 * track_width)
    
    # Calculate distance from optimal line
    if is_left_of_center:
        actual_distance_from_target = abs(distance_from_center + left_offset_target)
    else:
        actual_distance_from_target = distance_from_center - left_offset_target
    
    # Position reward
    if actual_distance_from_target <= marker_1:
        position_reward = 1.0
    elif actual_distance_from_target <= marker_2:
        position_reward = 0.5
    elif actual_distance_from_target <= marker_3:
        position_reward = 0.1
    else:
        position_reward = 1e-3
    
    # Calculate corner angle using waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.degrees(math.atan2(next_point[1] - prev_point[1], 
                                            next_point[0] - prev_point[0]))
    track_angle = abs(track_direction - heading)
    if track_angle > 180:
        track_angle = 360 - track_angle
    
    # Determine if in corner based on track angle
    is_corner = track_angle > 10
    
    # Speed reward based on corner severity
    if is_corner:
        # Calculate optimal speed for corner
        optimal_speed = 3.0 - (track_angle / 45.0)  # Speed reduces as corner angle increases
        optimal_speed = max(1.0, min(4.0, optimal_speed))  # Keep speed between 1 and 4
        
        # Reward for maintaining optimal corner speed
        speed_diff = abs(speed - optimal_speed)
        if speed_diff <= 0.5:
            speed_reward = 1.0
        elif speed_diff <= 1.0:
            speed_reward = 0.5
        else:
            speed_reward = 0.1
    else:
        # On straight sections, reward higher speeds
        speed_reward = min(1.0, speed/4.0)
    
    # Steering smoothness reward
    if is_corner:
        # Allow more steering in corners but still maintain smoothness
        if steering_angle <= 15:
            steering_reward = 1.0
        elif steering_angle <= 25:
            steering_reward = 0.5
        else:
            steering_reward = 0.1
    else:
        # Encourage minimal steering on straights
        if steering_angle <= 5:
            steering_reward = 1.0
        elif steering_angle <= 10:
            steering_reward = 0.5
        else:
            steering_reward = 0.1
    
    # Combine rewards with appropriate weights
    reward = (0.4 * position_reward +
             0.3 * speed_reward +
             0.3 * steering_reward)
    
    return float(reward)
