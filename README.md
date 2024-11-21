# raycast-py
This project implements a basic raycasting engine using Python and Pygame to simulate a 3D first-person perspective. It allows for simple movement within a 2D grid-based environment, where walls are rendered as vertical columns based on the player's viewpoint. The engine simulates a first-person camera with mouse look and keyboard navigation, enabling the user to explore the environment.

# Features:
Raycasting: Uses a raycasting algorithm to project a 3D view based on the player’s position and orientation.
Movement: Move forward, backward, and strafe left/right (A/D keys) within a grid environment.
Mouse Look: The player can look around by moving the mouse, with the camera turning based on mouse movement.
Collision Detection: The player cannot walk through walls. Movement is restricted by the map’s structure.
Customizable Parameters: Adjustable field of view, sensitivity, movement speed, and other parameters to tweak the experience.
Controls:
**W**: Move forward
**S**: Move backward
**A**: Strafe left
**D**: Strafe right
**Mouse Movement**: Look around
**Alt + F4/Cmd Q**: Exit
# Dependencies:
Python 3.x
Pygame
