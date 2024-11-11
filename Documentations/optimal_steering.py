# Calculate reward for alignment with optimal steering direction
heading = params['heading']
optimal_heading = math.degrees(math.atan2(y_forward - y, x_forward - x))
heading_diff = abs(optimal_heading - heading)
if heading_diff > 180:
    heading_diff = 360 - heading_diff
reward_alignment = math.cos(math.radians(heading_diff))
