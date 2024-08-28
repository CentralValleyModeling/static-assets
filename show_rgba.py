import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from PIL import Image

file = "images/favicon.ico"

with Image.open(file) as img:
    a = np.array(img.convert("RGBA"))

axs: list[Axes]
fig, axs = plt.subplots(ncols=a.shape[-1])
for i in range(a.shape[-1]):
    mpl_img = axs[i].imshow(a[:, :, i], vmin=0, vmax=255)
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.88, 0.15, 0.04, 0.7])
fig.colorbar(mpl_img, cax=cbar_ax)
plt.show()
