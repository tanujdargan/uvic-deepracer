# UVic DeepRacer

This repository contains the code and documentation for our team's participation in the DeepRacer Hackathon hosted at the University of Victoria (UVic). It includes training scripts, model configurations, reward functions, and other resources designed for AWS DeepRacer autonomous racing cars.

## Table of Contents

- [File Structure](#file-structure)
- [Usage](#usage)
- [Fastest Lap](#fastest-lap)

## File Structure

Here’s an overview of the repository’s main files and folders:

```
uvic-deepracer/
├── AWS DeepRacer Local Install Guide.md  # Guide for setting up AWS DeepRacer locally
├── README.md                             # This README file
├── assets/
│   └── fastest-lap.mp4                   # Video of the fastest lap
├── Documentations/
│   ├── follow_centre_line.py             # Reward function for following the center line
│   ├── model_metadata.json               # Metadata for the model
│   ├── optimal_path.py                   # Script to calculate optimal path
│   ├── optimal_steering.py               # Script to calculate optimal steering angles
│   ├── prevent_zig_zag.py                # Reward function to reduce zig-zag behavior
│   ├── reward-past.py                    # Example of a past reward function
│   ├── smooth_steering.py                # Reward function for smoother steering
│   ├── speed_curvature.py                # Script to calculate speed based on curvature
│   └── stay_on_track.py/
│       └── virtual_circuit.py            # Virtual circuit to keep the car on track
└── Reward Test Functions/
    ├── reward_function_one.py            # First custom reward function
    └── reward_function_two.py            # Second custom reward function
```

### AWS DeepRacer Local Install Guide.md
A guide to setting up AWS DeepRacer in a local environment. It includes installation steps and configuration instructions to streamline the development process.

### assets/
This folder contains media files related to the project, including a video of the fastest lap (`fastest-lap.mp4`).

### Documentations/
The `Documentations` directory contains various reward functions and scripts essential for the DeepRacer model's training and optimization:
- **follow_centre_line.py**: Reward function for guiding the car to follow the center line.
- **model_metadata.json**: Metadata for the DeepRacer model, defining configurations.
- **optimal_path.py** and **optimal_steering.py**: Scripts for computing the optimal path and steering, enhancing lap efficiency.
- **prevent_zig_zag.py**: Reward function to discourage zig-zag movements.
- **reward-past.py**: An example of a previous reward function.
- **smooth_steering.py**: Reward function to promote smoother steering adjustments.
- **speed_curvature.py**: Calculates speed based on track curvature.
- **stay_on_track.py/virtual_circuit.py**: A virtual circuit script to help keep the car on track.

### Reward Test Functions/
The `Reward Test Functions` directory includes custom reward functions designed and tested for different racing strategies:
- **reward_function_one.py**: Custom reward function focused on a specific strategy.
- **reward_function_two.py**: Alternative reward function emphasizing a different strategy.

## Usage

To test and evaluate custom reward functions, use the files in `Reward Test Functions/` on AWS DeepRacer with your own Hyperparameters or use ours.
Hyperparameters used:

| Hyperparameter                                                       | Value  |
|----------------------------------------------------------------------|--------|
| Gradient descent batch size                                          | 64     |
| Entropy                                                              | 0.01   |
| Discount factor                                                      | 0.999  |
| Loss type                                                            | Huber  |
| Learning rate                                                        | 0.0001 |
| Number of experience episodes between each policy-updating iteration | 20     |
| Number of epochs                                                     | 10     |

## Fastest Lap

https://github.com/user-attachments/assets/0543876f-d048-440a-a84d-a0fa33e393ed
