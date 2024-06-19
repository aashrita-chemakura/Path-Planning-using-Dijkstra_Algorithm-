# Path Planning using Dijkstra's Algorithm

This repository contains a Python-based path planning implementation using Dijkstra's algorithm. The project aims to provide a clear visualization of the algorithm at work by plotting the shortest path between a user-specified start and goal point in a given area, using technologies like OpenCV and NumPy.

## Prerequisites

Before running this project, ensure you have the following libraries installed:

- Numpy
- OpenCV
- time
- copy
- heapq

These can be installed via pip using the following command:

```bash
pip install numpy opencv-python
```
## Usage
To run the path planning algorithm:
1. Start the script via command line:
```bash
python path_planner.py
```
2. Follow the prompts to enter the X and Y coordinates for the start and goal points. Input should be integer values:
```bash
Enter X coordinate for the start point: <your_value>
Enter Y coordinate for the start point: <your_value>
Enter X coordinate for the goal point: <your_value>
Enter Y coordinate for the goal point: <your_value>
```
3.The algorithm will compute the shortest path and display it on your screen.
## Viewing Results
* The output path will be shown in a window upon completion of the algorithm's execution.
* Additionally, a video titled Successful-Test-Case.avi will be saved to the project directory, illustrating the path tracking.
* The exploration process may take up to 3 minutes, depending on your system's capabilities.
