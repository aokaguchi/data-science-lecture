#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace/intermediate'))
    print(os.getcwd())
except:
    pass

#%% [markdown]
# ## k-meansの仕組み
# ---
# クラスタ重心 (クラスタ内の学習サンプル平均) からの距離でデータを k 個に分割。
# 1. クラスタ中心を適当に選ぶ
# 1. データ点を一番距離の近いクラスタ中心に割り当てる
# 1. 割り当てられたデータ点に基づいてクラスタ中心を計算し直す
# 1. 2~3 を収束するまで繰り返す

#%%
from helpers.kmeans import algorithm
algorithm.show()

#%% [markdown]
# ## 注意点
# ---
# KMeans は初期値によって収束する結果が異なる。以下のように (KMeans の意図からすると) 適切ではない結果が得られることもあるので、`sklearn.cluster.KMeans`では複数の初期値を`n_init`回試して`inertia_` (各クラスタのサンプルから中心までの距離の合計) が最も小さいものを選択している。

#%%
from helpers.kmeans import inappropriate_example
inappropriate_example.show()
