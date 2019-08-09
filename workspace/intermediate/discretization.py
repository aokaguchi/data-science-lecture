#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace/intermediate'))
    print(os.getcwd())
except:
    pass

#%%
import numpy as np
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer
import seaborn as sns
from IPython.display import display
pd.set_option('max_rows', 5)

#%% [markdown]
# ## 離散化の効果
# ---
# 連続変数をカテゴリ変数化することを離散化という。
# 連続変数のほうが情報量が変数に含まれる情報は多いが、例えば年齢を 10 歳ごとの階級に分割するなどしたほうがデータの理解がしやすかったり、単純な線形でない関係を捉えられたりするため、離散化することがある。
#%% [markdown]
# ## 等間隔に分割
# ---
# 年齢を 10 歳ごとの階級に分割するなど、各階級の幅が等しくなるように分割。
#%% [markdown]
# ### Pythonでの等間隔階級への分割の実行方法
# ---
# `pandas.cut`または`sklearn.preprocessing.KBinsDiscretizer`を使用する。

#%%
fare = sns.load_dataset('titanic')['fare']
print('fare')
display(fare)

#%%
help(pd.cut)

#%%
pd.cut(fare, 5)

#%%
help(KBinsDiscretizer)

#%%
range_transformer = KBinsDiscretizer(n_bins=5,
                                     encode='ordinal',
                                     strategy='uniform')
range_transformer.fit(fare.values.reshape((-1, 1)))
edges = range_transformer.bin_edges_[0]
interval = [f'{edges[i]}~{edges[i+1]}' for i in range(edges.size - 1)]
print(f'interval: {interval}')
display(
    pd.Series(
        range_transformer.transform(fare.values.reshape((-1, 1))).ravel()))

#%% [markdown]
# ###### 練習問題
#
# `age`データセットを 0 歳 ~ 80 歳 まで 10 歳刻みで離散化する。 (`sklearn.preprocessing.KBinsDiscretizer`は間隔を指定できないので、`pandas.cut`を使用する)

#%%
age = sns.load_dataset('titanic')['age']
age.fillna(0.0, inplace=True)
print('age')
display(age)

#%%

#%% [markdown]
# ## 頻度で分割
# ---
# 各階級に含まれるサンプルの数が等しくなるように分割。
#%% [markdown]
# ### Pythonでの等頻度階級への分割の実行方法
# ---
# `pandas.qcut`または`sklearn.preprocessing.KBinsDiscretizer`を使用する。

#%%
help(pd.qcut)

#%%
# 四分位範囲で分割
pd.qcut(fare, 4, duplicates='drop')

#%%
help(KBinsDiscretizer)

#%%
quantile_transformer = KBinsDiscretizer(n_bins=4,
                                        encode='ordinal',
                                        strategy='quantile')
quantile_transformer.fit(fare.values.reshape((-1, 1)))
edges = quantile_transformer.bin_edges_[0]
interval = [f'{edges[i]}~{edges[i+1]}' for i in range(edges.size - 1)]
print(f'interval: {interval}')
display(
    pd.Series(
        quantile_transformer.transform(fare.values.reshape((-1, 1))).ravel()))

#%% [markdown]
# ###### 練習問題
#
# `age`データセットを四分位範囲で分割する。

#%%

#%% [markdown]
# ## クラスタリングを利用して分割
# ---
# 対象の変数にクラスタリングを適用し、その結果を利用して分割。
#%% [markdown]
# ### Pythonでのクラスタリングを利用した分割の実行方法
# ---
# `sklearn.preprocessing.KBinsDiscretizer`を使用する。 (使用されるクラスタリングは k-means)

#%%
help(KBinsDiscretizer)

#%%
cluster_transformer = KBinsDiscretizer(n_bins=3,
                                       encode='ordinal',
                                       strategy='kmeans')
cluster_transformer.fit(fare.values.reshape((-1, 1)))
edges = cluster_transformer.bin_edges_[0]
interval = [f'{edges[i]}~{edges[i+1]}' for i in range(edges.size - 1)]
print(f'interval: {interval}')
display(
    pd.Series(
        cluster_transformer.transform(fare.values.reshape((-1, 1))).ravel()))

#%% [markdown]
# ###### 練習問題
#
# `age`データセットを k-means クラスタリングで 3 分割する。

#%%
