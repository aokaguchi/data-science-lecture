import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
import seaborn as sns


def show():
    bins = [10, 30]
    tip = sns.load_dataset('tips')['tip']
    _, axes = plt.subplots(1, 2, figsize=figaspect(1 / 2))
    for ax, b in zip(axes, bins):
        ax.hist(tip, bins=b)
        ax.set(title=f'bins={b}', xticks=(), yticks=())
    plt.show()
