import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
from PIL import Image

# Create mesh grid
x = np.linspace(0, 100, 100)
y = np.linspace(0, 100, 100)
Luck, Hard_Work = np.meshgrid(x, y)

# Create a directory to store the images
output_dir = "success_frames"
os.makedirs(output_dir, exist_ok=True)

# Generate and save frames
frame_paths = []
for frame in range(11):
    lw = frame / 10
    hw = 1 - lw
    Success = ((Luck / 100) ** lw) * ((Hard_Work / 100) ** hw) * 100

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(Luck, Hard_Work, Success, cmap='viridis', edgecolor='none')
    ax.set_xlabel("Luck")
    ax.set_ylabel("Hard Work")
    ax.set_zlabel("Success")
    ax.set_title(f"Luck weight: {lw:.2f}, Hard Work weight: {hw:.2f}")
    ax.set_zlim(0, 100)
    plt.tight_layout()

    frame_path = os.path.join(output_dir, f"frame_{frame:02d}.png")
    plt.savefig(frame_path)
    plt.close()
    frame_paths.append(frame_path)

# Create GIF
images = [Image.open(fp) for fp in frame_paths]
gif_path = "success_surface.gif"
images[0].save(gif_path, save_all=True, append_images=images[1:], duration=500, loop=0)

print(f"GIF created successfully: {gif_path}")
