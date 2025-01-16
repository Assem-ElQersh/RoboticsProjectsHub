from collections import deque

import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot

room = np.zeros((5, 5), dtype=int)
room[2, 2:4] = -1
room[3, 2:4] = -1

start = (1, 0)
goal = (4, 4)

def bfs(grid, start, goal):
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == goal:
            break
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx, ny] != -1:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
    
    path = []
    current = goal
    while current:
        path.append(current)
        current = parent.get(current)
    path.reverse()
    return path

path = bfs(room, start, goal)

visual_room = np.copy(room)
visual_room[visual_room == 0] = 1
visual_room[visual_room == -1] = 0

fig = go.Figure()

fig.add_trace(go.Heatmap(
    z=visual_room,
    colorscale='Blues',
    showscale=False,
    name='Room',
    colorbar=dict(title="Room Layout", tickvals=[0, 1], ticktext=["Obstacle", "Empty"]),
))

fig.add_trace(go.Scatter(
    x=[start[1], goal[1]],
    y=[start[0], goal[0]],
    mode='markers',
    marker=dict(size=12, color=["green", "red"]),
    name="Start & Goal",
    text=["Start", "Goal"],
))

robot_path = go.Scatter(
    x=[start[1]] + [p[1] for p in path],
    y=[start[0]] + [p[0] for p in path],
    mode='markers+lines',
    marker=dict(size=12, color="yellow"),
    line=dict(color="yellow", width=2),
    name="Robot Path"
)

fig.add_trace(robot_path)

frames = []
for i in range(1, len(path)+1):
    x_values = [start[1]] + [p[1] for p in path[:i]]
    y_values = [start[0]] + [p[0] for p in path[:i]]
    
    frame = go.Frame(
        data=[
            go.Heatmap(z=visual_room, colorscale='Blues', showscale=False),
            go.Scatter(x=x_values, y=y_values, mode='markers+lines', marker=dict(size=12, color="yellow"), line=dict(color="yellow", width=2))
        ],
        name=f"Step {i}"
    )
    frames.append(frame)

fig.frames = frames

fig.update_layout(
    title="Robot Path Planning Animation",
    xaxis=dict(title="X Coordinate", tickvals=np.arange(5), ticktext=np.arange(5)),
    yaxis=dict(title="Y Coordinate", tickvals=np.arange(5), ticktext=np.arange(5)),
    updatemenus=[dict(
        type='buttons', showactive=False, buttons=[dict(label="Play", method="animate", args=[None, dict(frame=dict(duration=300, redraw=True), fromcurrent=True)])]
    )],
    autosize=False,
    width=800,
    height=700,
    xaxis_showgrid=False,
    yaxis_showgrid=False,
)

plot(fig)
