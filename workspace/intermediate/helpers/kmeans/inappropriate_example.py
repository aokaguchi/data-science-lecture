import numpy as np
from scipy.spatial.distance import cdist
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
import seaborn as sns


def show():
    blob_centers = np.array([(-5, -5), (0, 0), (5, 5)])
    cluster_centers = np.array([(-1, 1), (0, 0), (1, -1)])
    X, _ = make_blobs(n_samples=30,
                      centers=blob_centers,
                      shuffle=False,
                      random_state=1234)
    colors = np.array(sns.color_palette(n_colors=3))

    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.scatter(X[:, 0], X[:, 1], c='gray', alpha=0.4)
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    xx, yy = np.meshgrid(np.linspace(xmin, xmax, 100),
                         np.linspace(ymin, ymax, 100))
    mesh = np.c_[xx.ravel(), yy.ravel()]
    ax.scatter(mesh[:, 0],
               mesh[:, 1],
               c=colors[np.argmin(cdist(mesh, cluster_centers), axis=1)],
               alpha=0.2,
               marker='.')
    ax.scatter(cluster_centers[:, 0],
               cluster_centers[:, 1],
               c='white',
               marker='x')
    ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax), xticks=(), yticks=())
    plt.show()
