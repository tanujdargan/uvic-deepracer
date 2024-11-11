def reward_function(params):
    """
    Enhanced reward function for AWS DeepRacer with more granular center-line tracking
    and more drastic rewards/penalties
    """

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    steering_angle = abs(params['steering_angle'])
    is_offtrack = params.get('is_offtrack', False)
    is_crashed = params.get('is_crashed', False)

    # Initialize reward
    reward = 1.0

    # Severe penalty for off-track or crashed
    if is_offtrack or is_crashed:
        reward = 1e-6  # Even smaller penalty than before
        return float(reward)

    # Basic reward for staying on track
    if all_wheels_on_track:
        reward += 2.0
    else:
        reward = 1e-6
        return float(reward)

    # Define more granular markers from center
    markers = [
        0.05 * track_width,  # Super close to center
        0.1 * track_width,   # Very close to center
        0.15 * track_width,  # Close to center
        0.2 * track_width,   # Moderately close
        0.25 * track_width,  # Getting further
        0.35 * track_width,  # Far from center
        0.5 * track_width    # Very far from center
    ]

    # Exponentially decreasing rewards based on distance from center
    if distance_from_center <= markers[0]:
        reward += 1000.0  # Massive reward for perfect centering
    elif distance_from_center <= markers[1]:
        reward += 500.0   # Still excellent
    elif distance_from_center <= markers[2]:
        reward += 200.0   # Very good
    elif distance_from_center <= markers[3]:
        reward += 100.0   # Good
    elif distance_from_center <= markers[4]:
        reward += 20.0    # Acceptable
    elif distance_from_center <= markers[5]:
        reward += 5.0     # Poor
    elif distance_from_center <= markers[6]:
        reward += 1.0     # Very poor
    else:
        reward = 1e-6     # Practically off track
        return float(reward)

    # Enhanced speed incentive
    SPEED_THRESHOLD = 0.5
    MAX_SPEED = 1.0
    if speed >= SPEED_THRESHOLD:
        # Exponential reward for higher speeds when well-centered
        if distance_from_center <= markers[2]:  # Only reward high speeds when well-centered
            speed_ratio = (speed - SPEED_THRESHOLD) / (MAX_SPEED - SPEED_THRESHOLD)
            reward += (50.0 * speed_ratio)
    else:
        # Harsher penalty for slow speeds
        reward *= (speed / SPEED_THRESHOLD)

    # More aggressive steering penalty
    ABS_STEERING_THRESHOLD = 15.0
    if steering_angle > ABS_STEERING_THRESHOLD:
        steering_penalty = (steering_angle / 30)  # Normalize steering between 0 and 2
        reward *= (1.0 - steering_penalty)  # Can reduce reward by up to 100%

    # Enhanced progress incentive
    progress_reward = (progress * progress) / 100  # Quadratic progress reward
    reward += progress_reward

    # Huge completion bonus
    if progress == 100:
        reward += 1000.0  # Much bigger bonus for completing the lap

    # Ensure reward is within reasonable bounds
    reward = max(reward, 1e-6)
    
    return float(reward)
