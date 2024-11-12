import math

def reward_function(params):
    """
    Reward function that encourages optimal racing lines through corners,
    hitting the apex, maintaining higher speeds on straights,
    and slowing down appropriately for corners.
    """

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    x = params['x']  # Agent's current x position
    y = params['y']  # Agent's current y position
    speed = params['speed']
    heading = params['heading']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    track_width = params['track_width']
    steering_angle = abs(params['steering_angle'])  # Already an absolute value

    # Initialize reward
    reward = 1e-3  # Minimal reward

    # Terminate if off-track
    if not all_wheels_on_track:
        return reward

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    track_direction = math.atan2(
        next_point[1] - prev_point[1],
        next_point[0] - prev_point[0]
    )
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Calculate the curvature of the track
    # We can approximate curvature by comparing directions between waypoints
    # Get the indices for the waypoints ahead
    lookahead_points = 5  # Number of waypoints ahead to consider
    next_next_point = waypoints[min(closest_waypoints[1] + lookahead_points, len(waypoints) - 1)]

    track_direction_next = math.atan2(
        next_next_point[1] - next_point[1],
        next_next_point[0] - next_point[0]
    )
    track_direction_next = math.degrees(track_direction_next)

    # Calculate change in direction (curvature)
    curvature = abs(track_direction_next - track_direction)
    if curvature > 180:
        curvature = 360 - curvature

    # Define thresholds
    STRAIGHT_THRESHOLD = 5.0  # degrees change indicating a straight
    CURVE_THRESHOLD = 15.0    # degrees change indicating a curve
    HIGH_SPEED = 3.0  # m/s
    MEDIUM_SPEED = 2.0  # m/s
    LOW_SPEED = 1.0  # m/s

    # Base reward
    reward = 1.0

    ## Reward for maintaining optimal speed based on curvature
    if curvature < STRAIGHT_THRESHOLD:
        # On a straight, encourage high speed
        if speed >= HIGH_SPEED:
            speed_reward = 1.0
        else:
            speed_reward = speed / HIGH_SPEED
    elif curvature < CURVE_THRESHOLD:
        # On gentle curves, encourage medium speed
        if speed >= MEDIUM_SPEED:
            speed_reward = MEDIUM_SPEED / speed  # Slight penalty for too fast
        else:
            speed_reward = speed / MEDIUM_SPEED
    else:
        # On sharp curves, encourage low speed
        if speed <= LOW_SPEED:
            speed_reward = 1.0
        else:
            speed_reward = LOW_SPEED / speed  # Penalty for too fast

    reward *= speed_reward

    ## Reward for proper steering in curves
    # Encourage appropriate steering angles based on curvature
    if curvature >= CURVE_THRESHOLD:
        # In curves, encourage higher steering angles
        ideal_steering = curvature  # Approximate desired steering
        steering_diff = abs(ideal_steering - steering_angle)
        steering_reward = max(0.5, 1 - (steering_diff / 50))  # Scaled reward
    else:
        # On straights, keep steering angle small
        if steering_angle < 5:
            steering_reward = 1.0
        else:
            steering_reward = 0.8  # Slight penalty for unnecessary steering

    reward *= steering_reward

    ## Reward for alignment with track direction
    DIRECTION_THRESHOLD = 10.0  # degrees
    if direction_diff < DIRECTION_THRESHOLD:
        direction_reward = 1.0
    else:
        direction_reward = max(0.1, 1 - (direction_diff / 50))  # Penalty for misalignment

    reward *= direction_reward

    ## Penalty for being too far from center (optional)
    # Calculate distance from center
    distance_from_center = params['distance_from_center']
    max_distance = track_width * 0.5
    distance_ratio = distance_from_center / max_distance

    if distance_ratio <= 0.2:
        center_reward = 1.0  # Close to center, good
    elif distance_ratio <= 0.5:
        center_reward = 0.5  # Moderate distance, acceptable
    else:
        center_reward = 1e-3  # Likely off-track soon

    reward *= center_reward

    ## Small reward for making progress
    progress = params['progress']
    steps = params['steps']
    if steps > 0:
        progress_reward = (progress / steps) * 100  # Scale to a reasonable value
        reward += progress_reward

    # Ensure the reward is positive
    reward = max(reward, 1e-3)

    return float(reward)
