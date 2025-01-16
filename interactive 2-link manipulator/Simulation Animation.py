import math
from tkinter import Button, Entry, Label, StringVar, Tk, messagebox

import plotly.graph_objects as go

# Constants
L1 = 5
L2 = 4
angles_list = []
reachable_points = []

def inverse_kinematics(x, y):
    """Solve inverse kinematics for the given x, y coordinates."""
    d = math.sqrt(x**2 + y**2)
    if d > (L1 + L2):
        return None
    cos_theta2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    if abs(cos_theta2) > 1:
        return None
    sin_theta2 = math.sqrt(1 - cos_theta2**2)
    theta2 = math.atan2(sin_theta2, cos_theta2)
    k1 = L1 + L2 * cos_theta2
    k2 = L2 * sin_theta2
    theta1 = math.atan2(y, x) - math.atan2(k2, k1)
    return math.degrees(theta1), math.degrees(theta2)

def visualize_highlighted_touched_points():
    """Visualize the manipulator highlighting points it touches along the line."""
    frames = []
    x_arm = []
    y_arm = []

    # Generate the full line
    x_full = [i for i in range(-20, 21)]  # Extend the range to show the full line
    y_full = [-x / 2 + 10 for x in x_full]

    # Extract the reachable points
    x_reachable = [p[0] for p in reachable_points]
    y_reachable = [p[1] for p in reachable_points]

    # Create the color list for the reachable points
    colors = ['gray'] * len(x_reachable)  # Start with all points as gray

    # Calculate manipulator positions for each point
    for i, (theta1, theta2) in enumerate(angles_list):
        x0, y0 = 0, 0  # Origin
        x1 = x0 + L1 * math.cos(math.radians(theta1))
        y1 = y0 + L1 * math.sin(math.radians(theta1))
        x2 = x1 + L2 * math.cos(math.radians(theta1 + theta2))
        y2 = y1 + L2 * math.sin(math.radians(theta1 + theta2))

        x_arm.append([x0, x1, x2])
        y_arm.append([y0, y1, y2])

        # Update the color of the current point being touched
        colors[i] = 'red'

        # Create a frame for each position
        frames.append(go.Frame(
            data=[
                # Original full line (persistent in every frame)
                go.Scatter(x=x_full, y=y_full, mode="lines",
                           line=dict(color="gray", width=2), name="Full Function Line"),
                # Manipulator arm
                go.Scatter(x=[x0, x1, x2], y=[y0, y1, y2], mode="lines+markers",
                           line=dict(color="blue", width=5), name="Manipulator Arm"),
                # Highlighted points touched by the arm
                go.Scatter(x=x_reachable, y=y_reachable, mode="markers",
                           marker=dict(color=colors, size=10), name="Tracked Points"),
            ],
            name=f"frame{i}"
        ))

    # Create the figure layout
    fig = go.Figure(
        data=[
            # Initial manipulator arm
            go.Scatter(x=[0, 0, 0], y=[0, 0, 0], mode="lines+markers",
                       line=dict(color="blue", width=5), name="Manipulator Arm"),
            # Original full line
            go.Scatter(x=x_full, y=y_full, mode="lines",
                       line=dict(color="gray", width=2), name="Full Function Line"),
            # Initial points (all gray)
            go.Scatter(x=x_reachable, y=y_reachable, mode="markers",
                       marker=dict(color='gray', size=10), name="Tracked Points"),
        ],
        layout=go.Layout(
            title="2-Link Manipulator with Highlighted Points",
            xaxis=dict(title="X (cm)", range=[-25, 25]),
            yaxis=dict(title="Y (cm)", range=[-10, 20]),
            updatemenus=[
                dict(
                    type="buttons",
                    showactive=True,
                    buttons=[
                        dict(label="Start", method="animate",
                             args=[None, dict(frame=dict(duration=200, redraw=True), fromcurrent=True)]),
                    ],
                )
            ],
        ),
        frames=frames
    )

    fig.show()

def main():
    def calculate_and_solve():
        try:
            global angles_list, reachable_points
            x_start = float(x_start_var.get())
            x_end = float(x_end_var.get())
            step = float(step_var.get())

            if step <= 0:
                raise ValueError("Step size must be positive.")
            if x_start >= x_end:
                raise ValueError("Start X must be less than End X.")

            angles_list.clear()
            reachable_points.clear()

            x = x_start
            while x <= x_end:
                y = -x / 2 + 10
                if math.sqrt(x**2 + y**2) <= (L1 + L2):
                    angles = inverse_kinematics(x, y)
                    if angles is not None:
                        angles_list.append(angles)
                        reachable_points.append((x, y))
                x += step

            if not reachable_points:
                messagebox.showerror("Error", "No reachable points found.")
            else:
                max_length = sum(math.sqrt((reachable_points[i][0] - reachable_points[i - 1][0])**2 +
                                           (reachable_points[i][1] - reachable_points[i - 1][1])**2)
                                 for i in range(1, len(reachable_points)))
                messagebox.showinfo(
                    "Result",
                    f"Maximum length tracked: {max_length:.2f} cm. Press 'Visualize' to view the tracking.",
                )
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def proceed_to_visualize():
        if not angles_list:
            messagebox.showerror("Error", "No angles to visualize. Solve the problem first.")
        else:
            visualize_highlighted_touched_points()

    root = Tk()
    root.title("Inverse Kinematics Solver")
    root.geometry("400x300")

    x_start_var = StringVar(value="0")
    x_end_var = StringVar(value="10")
    step_var = StringVar(value="0.2")

    Label(root, text="X Start (cm):").grid(row=0, column=0, pady=5, ipadx=10)
    Entry(root, textvariable=x_start_var).grid(row=0, column=1)

    Label(root, text="X End (cm):").grid(row=1, column=0, pady=5, ipadx=10)
    Entry(root, textvariable=x_end_var).grid(row=1, column=1)

    Label(root, text="Step Size (cm):").grid(row=2, column=0, pady=5, ipadx=10)
    Entry(root, textvariable=step_var).grid(row=2, column=1)

    Button(root, text="Solve", command=calculate_and_solve).grid(row=3, column=0, pady=20, ipadx=10)
    Button(root, text="Visualize", command=proceed_to_visualize).grid(row=3, column=1, pady=20, ipadx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
