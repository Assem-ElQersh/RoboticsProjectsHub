import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import RadioButtons, Slider


def rotate(x, y, theta):
    theta_rad = np.radians(theta)
    cos_theta = np.cos(theta_rad)
    sin_theta = np.sin(theta_rad)
    x_rot = cos_theta * x - sin_theta * y
    y_rot = sin_theta * x + cos_theta * y
    return x_rot, y_rot

def update(val):
    func = func_radio.value_selected
    theta = angle_slider.val
    if func == 'sin':
        y = np.sin(x)
    elif func == 'cos':
        y = np.cos(x)
    elif func == 'tan':
        y = np.tan(x)
    y_rot = rotate(x, y, theta)[1]
    
    original_line.set_ydata(y)
    line.set_ydata(y_rot)
    line.set_label(f'Rotated {func} by {theta:.0f}°')
    ax.set_title(f'Interactive Rotation of $y = {func}(x)$ by {theta:.0f}° Counterclockwise')
    fig.canvas.draw_idle()

fig, ax = plt.subplots(figsize=(12, 6))
plt.subplots_adjust(left=0.3, bottom=0.25)

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)

original_line, = ax.plot(x, y, label='Original', color='blue')
line, = ax.plot(x, y, linestyle='--', color='orange')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)
ax.set_aspect('equal', adjustable='datalim')
ax.autoscale_view()

angle_slider = Slider(plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow'), 'Rotation Angle', 0, 360, valinit=0)
angle_slider.on_changed(update)

func_radio = RadioButtons(plt.axes([0.05, 0.3, 0.15, 0.15], facecolor='lightgoldenrodyellow'), ('sin', 'cos', 'tan'))
func_radio.on_clicked(update)

plt.show()
