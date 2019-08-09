import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
import seaborn as sns
from ipywidgets import interactive_output, IntSlider, Play, jslink
from IPython.display import display

np.random.seed(1234)
sample = np.random.chisquare(df=3, size=6)
sample.sort()
x = np.linspace(-2, 7, 50)
y = stats.norm.pdf(x.reshape((-1, 1)), loc=sample).sum(axis=1)
colors = sns.color_palette()[:sample.size]


def plot(step):
    loc = x[step - 1]
    distribution = stats.norm(loc=loc)
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.plot(x, distribution.pdf(x))
    ax.plot(x[:step], y[:step], color='black', alpha=0.3)
    density = distribution.pdf(sample)
    cumsum = np.hstack([[0], density.cumsum()])
    ax.vlines(sample, 0, density, color=colors)
    ax.vlines(np.repeat(loc, sample.size),
              cumsum[:-1],
              cumsum[1:],
              color=colors,
              alpha=0.3)
    ax.set(xlabel='x', xticks=(), xlim=(x.min(), x.max()), ylim=(0, 1))
    plt.show()


def show():
    step = IntSlider(value=1, min=1, max=x.size)
    play = Play(interval=200, value=1, min=1, max=x.size, step=1)
    jslink((play, 'value'), (step, 'value'))
    output = interactive_output(plot, dict(step=step))
    display(play, output)
