#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace/intermediate'))
    print(os.getcwd())
except:
    pass

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
pd.set_option('max_rows', 7)

#%% [markdown]
# ## ヒートマップ
# ---
# 二次元グラフ上で、値を色で表したもの。
# 二次元グラフの軸はクロス集計表のような質的変数でも、座標 (地図など) のような量的変数でもよい。
# 色で表す値は主に量的変数 (色の濃淡で表現) が用いられるが、質的変数 (色の違いで表現) でもよい。

#%%
titanic = sns.load_dataset('titanic')
print('titanic')
display(titanic)


#%%
table = pd.pivot_table(
    titanic,
    values='fare',
    index='class',
    columns='embark_town',
    aggfunc='median')
print('乗船地・等級ごとの料金の中央値')
display(table)


#%%
sns.heatmap(table, cmap='Reds')
plt.show()

#%% [markdown]
# ### Pythonでのヒートマップ表示
# ---
# `seaborn.heatmap`を使用する。 (二次元グラフが地図などの場合は散布図などを使用する)
# カラーマップは色の濃淡などが値の大小を表すようなものを指定する。

#%%
help(sns.heatmap)


#%%
sns.heatmap(
    pd.pivot_table(titanic, values='survived', index='class', columns='sex'),
    cmap='Reds')
plt.show()

#%% [markdown]
# ###### 練習問題
#
# `titanic`データセットで、縦軸に`class`・横軸に`sex`をとったクロス集計表をヒートマップで表示する。

#%%

#%% [markdown]
# 使用する場面は限られているが、表中の値を縦軸・横軸のカテゴリで階層的クラスタリングを実施した結果と併せて表示するなどの方法もある。

#%%
tips = sns.load_dataset('tips').query('1 < size < 5')
print('tips')
display(tips)


#%%
table = pd.pivot_table(tips, values='total_bill', index='day', columns='size')
display(table)


#%%
sns.clustermap(table, cmap='Reds')
plt.show()

#%% [markdown]
# ## 散布図行列
# ---
# 3 つ以上の変数があるデータセットで、 2 つの変数の組み合わせ全てに対して散布図を作成したもの。対角 (同じ変数同士) にはヒストグラムを配置したりする。

#%%
iris = sns.load_dataset('iris')
print('iris')
display(iris)


#%%
sns.pairplot(iris)
plt.show()

#%% [markdown]
# ### Pythonでの散布図行列表示
# ---
# `pandas.plotting.scatter_matrix`や`seaborn.pairplot`を用いる。

#%%
tips = sns.load_dataset('tips')
print('tips')
display(tips)


#%%
help(pd.plotting.scatter_matrix)


#%%
pd.plotting.scatter_matrix(tips)
plt.show()


#%%
help(sns.pairplot)


#%%
sns.pairplot(tips)
plt.show()

#%% [markdown]
# ###### 練習問題
#
# `crashes`データセットの散布図行列を表示する。

#%%
crashes = sns.load_dataset('car_crashes')
print('crashes')
display(crashes)


#%%

#%% [markdown]
# ## 相関行列
# ---
# 散布図行列のように 2 つの変数の組み合わせ全てに対して相関係数を集計したもの。
# 変数が多く全ての変数の散布図行列を表示しにくい場合に、代わりに利用することもある。ただし、相関係数では捉えられない関係もあるので、必ず最後は散布図も確認する。

#%%
iris.corr()

#%% [markdown]
# ### Pythonでの相関行列作成
# ---
# `pandas.DataFrame.corr`を利用する。

#%%
help(pd.DataFrame.corr)


#%%
tips.corr()

#%% [markdown]
# ###### 練習問題
#
# `crashes`データセットの相関行列を作成する。

#%%

#%% [markdown]
# ## 様々な可視化手法の組み合わせ
#%% [markdown]
# ### 相関行列とヒートマップ
# ---
# 色によって相関係数を把握しやすくなるので、相関行列をヒートマップにすることがよくある。
# デフォルトの設定でヒートマップを作成すると、相関行列の最小値・最大値を色の下限・上限に使用してしまい、中心が 0 にならなかったり、全体に相関関係が低いのに高いものがあるように感じたり、誤解が生じやすい。また、色もデフォルトだと相関関係を把握しにくい。必ず**`vmin`, `vmax`は -1, 1** に設定し、**`cmap`も中央が薄く、最小や最大に近づくほど色が濃い**ものを使用する。

#%%
sns.heatmap(iris.corr(), vmin=-1, vmax=1, cmap='seismic', annot=True)
plt.show()

#%% [markdown]
# ###### 練習問題
#
# `tips`データセットの相関行列をヒートマップで表示する。

#%%

#%% [markdown]
# ### 散布図行列と相関行列
# ---
# 散布図行列も相関行列も右上三角部分と左下三角部分は全く同じ情報を表しており、情報としては無駄になる。そこで、半分を散布図行列に、残り半分を相関行列にすると無駄がない。

#%%
def corr_scatter_matrix(data, height=1.5, cmap='seismic', **kwargs):
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.colors import Normalize
    from matplotlib.cm import ScalarMappable
    import seaborn as sns

    def corr(x, y, label, color, **kwargs):
        corr_ = np.corrcoef(x, y)[0, 1]
        norm = Normalize(vmin=kwargs.pop('vmin') if 'vmin' in kwargs else -1,
                         vmax=kwargs.pop('vmax') if 'vmax' in kwargs else 1)
        cmap = plt.get_cmap(kwargs.pop('cmap') if 'cmap' in kwargs else None)
        sm = ScalarMappable(norm, cmap)
        ax = plt.gca()
        ax.text(0.5, 0.5, '{:.2f}'.format(corr_), transform=ax.transAxes,
                horizontalalignment='center', verticalalignment='center',
                **kwargs)
        ax.set(facecolor=sm.to_rgba(corr_))

    matrix = sns.PairGrid(data, height=height)
    matrix.map_upper(corr, cmap=cmap, **kwargs)
    matrix.map_lower(plt.scatter)
    matrix.map_diag(sns.distplot)
    plt.show()

corr_scatter_matrix(iris)

#%% [markdown]
# ### 散布図行列とカテゴリ変数
# ---
# カテゴリ変数は同じ値が多いため、単純に散布図などを描くと特徴を掴みにくい。

#%%
sns.stripplot('day', 'total_bill', data=tips, jitter=False)
plt.show()

#%% [markdown]
# そこで、以下のようなグラフを用いる。
#%% [markdown]
# #### ストリッププロット
# ---
# 値に小さな乱数を加えて少しずつずらすことで、値の重なり具合をわかりやすくしたもの。
# `seaborn.stripplot`を使用する。

#%%
help(sns.stripplot)


#%%
sns.stripplot('day', 'total_bill', data=tips)
plt.show()

#%% [markdown]
# #### バイオリンプロット
# ---
# 値の重なり具合をデータの分布として表したもの。
# `seaborn.violinplot`を使用する。

#%%
help(sns.violinplot)


#%%
sns.violinplot('day', 'total_bill', data=tips)
plt.show()

#%% [markdown]
# ### 全変数の可視化
# ---
# 上の散布図行列と相関行列を組み合わせた図をカテゴリ変数にも対応させた、以下のような関数を用意しておくとよい。

#%%
def pairplot(df, **kwargs):
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.figure import figaspect
    import seaborn as sns

    def corrplot(x, y, data, cmap='coolwarm', correlation='spearman',
                 **kwargs):
        from scipy import stats
        from matplotlib.patches import Ellipse

        data_x = data[x]
        data_y = data[y]
        is_x_category = data_x.dtype.name == 'category'
        is_y_category = data_y.dtype.name == 'category'
        if is_x_category:
            data_x = data_x.cat.codes
        if is_y_category:
            data_y = data_y.cat.codes
        if correlation is 'pearson' or not is_x_category or not is_y_category:
            method = 'pearson'
        else:
            method = 'spearman'
        r = data_x.corr(data_y, method=method)
        if type(cmap) is str:
            cmap = plt.get_cmap(cmap)
        color = cmap((r + 1) / 2)
        ax.axis('off')
        ax.add_artist(
            Ellipse((0.5, 0.5),
                    width=np.sqrt(1 + r),
                    height=np.sqrt(1 - r),
                    angle=45,
                    color=color))
        ax.text(
            0.5,
            0.5,
            '{:.2f}'.format(r),
            size='x-large',
            horizontalalignment='center',
            verticalalignment='center')

    def crosstabplot(x, y, data, ax, **kwargs):
        import pandas as pd

        cross = pd.crosstab(data[x], data[y]).values
        size = cross / cross.max() * 500
        crosstab_kws = kwargs[
            'crosstab_kws'] if 'crosstab_kws' in kwargs else {}
        scatter_kws = dict(color=sns.color_palette()[0], alpha=0.3)
        scatter_kws.update(crosstab_kws['scatter_kws'] if 'scatter_kws' in
                           crosstab_kws else {})
        text_kws = dict(size='x-large')
        text_kws.update(crosstab_kws['text_kws'] if 'text_kws' in
                        crosstab_kws else {})
        for (xx, yy), count in np.ndenumerate(cross):
            ax.scatter(xx, yy, s=size[xx, yy], **scatter_kws)
            ax.text(
                xx,
                yy,
                count,
                horizontalalignment='center',
                verticalalignment='center',
                **text_kws)

    def show_off_legend(ax):
        legend = ax.get_legend()
        if legend:
            legend.set(visible=False)

    n_variables = df.columns.size
    hue = kwargs['hue'] if 'hue' in kwargs else None
    figsize = kwargs['figsize'] if 'figsize' in kwargs else figaspect(
        1) * 0.5 * n_variables
    _, axes = plt.subplots(n_variables, n_variables, figsize=figsize)
    plt.subplots_adjust(hspace=0.1, wspace=0.1)

    for i in range(n_variables):
        axes[i, i].get_shared_x_axes().join(*axes[i:n_variables, i])
        if i > 1:
            axes[i, 0].get_shared_y_axes().join(*axes[i, :i - 1])

    for (row, col), ax in np.ndenumerate(axes):
        x = df.columns[col]
        y = df.columns[row]
        x_data = df[x]
        y_data = df[y]
        x_dtype = x_data.dtype.name
        y_dtype = y_data.dtype.name
        is_x_category = x_dtype == 'category'
        is_y_category = y_dtype == 'category'
        if is_x_category:
            x_categories = x_data.cat.categories
        if is_y_category:
            y_categories = y_data.cat.categories

        if row == col:  # diagonal
            hue_data = df[hue] if hue else None
            if is_x_category:
                bar_kws = dict(alpha=0.4, orientation='vertical')
                bar_kws.update(kwargs['bar_kws'] if 'bar_kws' in
                               kwargs else {})
                if hue:
                    cross = pd.crosstab(x_data, hue_data)
                    cross.index = cross.index.categories
                    if hue_data.dtype.name == 'category':
                        cross.columns = cross.columns.categories
                    else:
                        cross.columns = hue_data.unique()
                    cross.reset_index(inplace=True)
                    melt = pd.melt(cross, id_vars='index', var_name='hue')
                    hue_values = melt['hue'].unique()
                    colors = sns.color_palette(n_colors=hue_values.size)
                    for i in range(hue_values.size):
                        hue_value = hue_values[i]
                        color = colors[i]
                        subset = melt[melt['hue'] == hue_value]
                        if i is 0:
                            bottom = 0
                        else:
                            bottom = melt.loc[melt['hue'].isin(
                                hue_values[:i])].groupby('index').sum().loc[
                                    subset['index']].values.ravel()
                        ax.bar(
                            subset['index'],
                            subset['value'],
                            bottom=bottom,
                            color=color,
                            **bar_kws)
                else:
                    cross = pd.crosstab(x_data, []).values.ravel()
                    sns.barplot(
                        x_data.cat.categories,
                        cross,
                        color=sns.color_palette()[0],
                        ci=None,
                        ax=ax,
                        **bar_kws)
            else:
                dist_kws = kwargs['dist_kws'] if 'dist_kws' in kwargs else {}
                if hue:
                    colors = sns.color_palette(n_colors=hue_data.unique().size)
                    hist_kws = dict(color=colors, alpha=0.4)
                    hist_kws.update(dist_kws['hist_kws'] if 'hist_kws' in
                                    dist_kws else {})
                    if hue_data.dtype.name == 'category':
                        hue_values = df[hue].cat.categories
                    else:
                        hue_values = df[hue].unique()
                    ax.hist([df.loc[df[hue] == v, x] for v in hue_values],
                            density=True,
                            histtype='barstacked',
                            **hist_kws)
                    for c, v in zip(colors, hue_values):
                        sns.distplot(
                            df.loc[df[hue] == v, x],
                            hist=False,
                            color=c,
                            ax=ax,
                            **dist_kws)
                else:
                    sns.distplot(x_data, ax=ax, **dist_kws)
        elif row < col:  # upper
            corr_kws = kwargs['corr_kws'] if 'corr_kws' in kwargs else {}
            corrplot(x, y, data=df, **corr_kws)
        else:  # lower
            if is_x_category and is_y_category:
                crosstabplot(x, y, data=df, ax=ax)
            else:
                violin_kws = kwargs[
                    'violin_kws'] if 'violin_kws' in kwargs else {}
                if is_x_category or is_y_category:
                    orient = 'v' if is_x_category else 'h'
                    sns.violinplot(
                        x, y, hue, df, orient=orient, ax=ax, **violin_kws)
                    show_off_legend(ax)
                else:
                    scatter_kws = kwargs[
                        'scatter_kws'] if 'scatter_kws' in kwargs else {}
                    sns.scatterplot(x, y, hue, data=df, ax=ax, **scatter_kws)
                    show_off_legend(ax)

        if row < n_variables - 1:
            ax.set(xlabel='')
            for ticklabel in ax.get_xticklabels():
                ticklabel.set(visible=False)
        else:
            ax.set(xlabel=x)
            if is_x_category:
                ax.set(
                    xticks=np.arange(x_categories.size),
                    xticklabels=x_data.cat.categories)
        if col > 0:
            ax.set(ylabel='')
            for ticklabel in ax.get_yticklabels():
                ticklabel.set(visible=False)
        else:
            ax.set(ylabel=y)
            if row > 0 and is_y_category:
                ax.set(
                    yticks=np.arange(y_categories.size),
                    yticklabels=y_data.cat.categories)
    return axes


#%%
tips.loc[:, 'sex':'size'] = tips.loc[:, 'sex':'size'].astype('category')
pairplot(tips)
plt.show()

#%% [markdown]
# ## 平行座標プロット
# ---
# 横軸に各変数・縦軸に値をとり、同じサンプルの値を線で結んだグラフ。
# 他と傾向の違う変数を見つけたり、特定の条件のサンプル群の傾向を見つけたりするのに役立つ。

#%%
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
init_notebook_mode()

iris['species'] = pd.Categorical(iris['species'], ordered=True).codes
fig = go.Figure(data=[
    go.Parcoords(dimensions=[
        dict(
            range=[iris[col].min(), iris[col].max()],
            label=col,
            values=iris[col]) for col in iris.columns
    ])
])

iplot(fig)
