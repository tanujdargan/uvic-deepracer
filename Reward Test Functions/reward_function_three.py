def reward_function(params):
    '''
    Example of rewarding the agent to stay on the left side of the center line.
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']

    # Offset to the left side of the center line (10% of the track width to the left)
    left_offset_target = -0.3 * track_width

    # Calculate markers at varying distances from the left offset target
    marker_1 = abs(left_offset_target - 0.1 * track_width)
    marker_2 = abs(left_offset_target - 0.25 * track_width)
    marker_3 = abs(left_offset_target - 0.5 * track_width)

    # Determine actual distance from the desired left-side target line
    if is_left_of_center:
        # If the car is to the left of the center, distance is closer to the target line
        actual_distance_from_target = abs(distance_from_center + left_offset_target)
    else:
        # If the car is to the right of the center, distance is increased to encourage moving left
        actual_distance_from_target = distance_from_center - left_offset_target

    # Give higher reward if the car is closer to the left-side target line
    if actual_distance_from_target <= marker_1:
        reward = 1.0
    elif actual_distance_from_target <= marker_2:
        reward = 0.5
    elif actual_distance_from_target <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # Likely crashed or far off the left target line

    return float(reward)
