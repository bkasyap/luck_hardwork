import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.set_page_config(layout="wide")
st.title("Luck vs Hard Work: Success Simulator")

# Sliders for weight adjustment
luck_weight = st.slider("Luck Weight", 0.1, 1.0, 0.5, 0.1)
hard_work_weight = st.slider("Hard Work Weight", 0.1, 1.0, 0.5, 0.1)

# Normalize weights
total_weight = luck_weight + hard_work_weight
lw = luck_weight / total_weight
hw = hard_work_weight / total_weight

# Generate mesh grid
x = np.linspace(0, 100, 100)
y = np.linspace(0, 100, 100)
Luck, Hard_Work = np.meshgrid(x, y)

# Calculate Success
Success = ((Luck / 100) ** lw) * ((Hard_Work / 100) ** hw) * 100

# Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(Luck, Hard_Work, Success, cmap='viridis', edgecolor='none')
ax.set_xlabel("Luck")
ax.set_ylabel("Hard Work")
ax.set_zlabel("Success")
ax.set_title(f"Success Surface\n(Luck weight: {lw:.2f}, Hard Work weight: {hw:.2f})")
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Success Level')

# Display in Streamlit
st.pyplot(fig)
