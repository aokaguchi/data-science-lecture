import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from matplotlib.patches import Circle, Arc


def show():
    theta = np.pi / 3
    points = np.array([[2, 0], [3 * np.cos(theta), 3 * np.sin(theta)]])
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    line_prop = dict(color='black', alpha=0.2)
    ax.axhline(0, **line_prop)
    ax.axvline(0, **line_prop)
    line_prop['linestyles'] = '--'

    def scatter_with_annotation(ax, text, point):
        ax.scatter(*point, color='gray')
        ax.plot((0, point[0]), (0, point[1]), color='gray')
        ax.text(point[0], point[1] + 0.1, text, horizontalalignment='left')

    scatter_with_annotation(ax, 'A', points[0])
    scatter_with_annotation(ax, 'B', points[1])
    ax.add_patch(
        Circle((0, 0), radius=1, alpha=0.4, fill=False, linestyle='--'))
    ax.add_patch(Arc((0, 0), 2, 2, theta2=np.degrees(theta)))
    ax.text(np.cos(theta) / 2,
            np.sin(theta) / 2,
            1,
            horizontalalignment='center',
            verticalalignment='bottom')
    ax.plot((0, np.cos(theta)), (0, 0), color='red')
    ax.vlines(np.cos(theta), 0, np.sin(theta), color='gray', linestyles='--')
    ax.text(np.cos(theta) / 2,
            0,
            r'$cos\theta$',
            size='large',
            color='red',
            horizontalalignment='center',
            verticalalignment='top')
    ax.set(xlim=(-0.5, 3), ylim=(-0.5, 3), xticks=(0, ), yticks=(0, ))
    plt.show()
