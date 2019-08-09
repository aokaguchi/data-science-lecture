import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
import seaborn as sns
from ipywidgets import interactive_output, IntSlider, Play, jslink
from IPython.display import display

np.random.seed(1234)
sample = np.random.chisquare(df=3, size=6)
x = np.linspace(-2, 7, 50).reshape((-1, 1))


def plot(count):
    distributions = stats.norm(loc=sample[:count])
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.plot(x, distributions.pdf(x))
    ax.plot(x, distributions.pdf(x).sum(axis=1), color='black', alpha=0.3)
    sns.rugplot(sample, color='black', ax=ax)
    ax.set(xlabel='x', xticks=(), xlim=(x.min(), x.max()), ylim=(0, 1))
    plt.show()


def show():
    count = IntSlider(value=1, min=1, max=sample.size)
    play = Play(interval=1000, value=1, min=1, max=sample.size, step=1)
    jslink((play, 'value'), (count, 'value'))
    output = interactive_output(plot, dict(count=count))
    display(play, output)
