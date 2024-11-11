def reward_function(params):
    """
    Reward function for AWS DeepRacer
    """

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']           # Boolean, True if all wheels are on track
    track_width = params['track_width']                           # Width of the track
    distance_from_center = params['distance_from_center']         # Distance from the center line
    speed = params['speed']                                       # Agent's speed in m/s
    progress = params['progress']                                 # Percentage of track completed
    steps = params['steps']                                       # Number of steps completed
    steering_angle = abs(params['steering_angle'])                # Steering angle, absolute value
    is_offtrack = params.get('is_offtrack', False)                # Boolean, True if the agent is off track
    is_crashed = params.get('is_crashed', False)                  # Boolean, True if the agent has crashed

    # Initialize reward
    reward = 1.0

    # Penalize if the car is off-track or crashed
    if is_offtrack or is_crashed:
        reward = 1e-3  # Minimal reward
        return float(reward)

    # Reward if all wheels are on track
    if all_wheels_on_track:
        reward += 1.0
    else:
        # Penalize if the car goes off track
        reward = 1e-3
        return float(reward)

    # Calculate markers at varying distances from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Reward proportional to the distance from the center line
    if distance_from_center <= marker_1:
        # Closest to center line
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        # Likely crashed/close to off track
        reward = 1e-3
        return float(reward)

    # Speed incentive
    SPEED_THRESHOLD = 2.0  # Define a speed threshold
    if speed >= SPEED_THRESHOLD:
        # High speed reward
        reward += 1.0
    else:
        # Penalize slow speeds
        reward += (speed / SPEED_THRESHOLD)

    # Steering penalty threshold, change in degrees
    ABS_STEERING_THRESHOLD = 15.0

    # Penalize if the agent is steering too much
    if steering_angle > ABS_STEERING_THRESHOLD:
        steering_penalty = (steering_angle / 60)  # Normalize steering between 0 and 1
        reward *= (1.0 - steering_penalty)

    # Progress incentive, encourage completing the track
    if progress == 100:
        reward += 10.0  # Big bonus for completing the lap

    # Ensure reward is within reasonable bounds
    reward = max(reward, 1e-3)

    return float(reward)
