import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(2,1,1)


# fig2 = plt.figure()
# ax2 = fig2.add_axes([0.15, 0.1, 0.7, 0.3])

import numpy as np
t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax.plot(t, s, color='blue', lw=2)

# xtext = ax.set_xlabel('my xdata')
# ytext = ax.set_ylabel('my ydata')

plt.show(ax)