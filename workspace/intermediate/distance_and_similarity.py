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
from scipy.spatial.distance import euclidean, cityblock, cosine
from sklearn.metrics.pairwise import paired_euclidean_distances, paired_manhattan_distances, cosine_similarity

#%% [markdown]
# ## ユークリッド距離
# ---
# 一般的な距離。
# 2 点 $A=( a_{1} ,a_{2} ,\dotsc ,a_{n}) ,B( b_{1} ,b_{2} ,\dotsc ,b_{n})$ 間の距離は $\displaystyle d=\sqrt{\sum ^{n}_{i=1}( a_{i} -b_{i})^{2}}$ で表される。
#%% [markdown]
# ### Pythonでのユークリッド距離の求め方
# ---
# `scipy.spatial.distance.euclidean`または`sklearn.metrics.pairwise.paired_euclidean_distances`を使用する。`paired_euclidean_distances`は入力に行列を想定しているので、ベクトル同士の距離の場合は $1\times 要素数$ の形にしてから実行する。

#%%
np.random.seed(1234)
a = np.random.uniform(0, 3, 3)
b = np.random.uniform(5, 10, 3)
print(f'a={a}')
print(f'b={b}')

#%%
euc = np.sqrt(np.sum((a - b)**2))

#%%
help(euclidean)

#%%
np.isclose(euc, euclidean(a, b))

#%%
help(paired_euclidean_distances)

#%%
np.isclose(euc,
           paired_euclidean_distances(a.reshape((1, -1)), b.reshape((1, -1))))

#%% [markdown]
# ## マンハッタン距離
# ---
# 碁盤状の道をたどる場合の距離。
# 2 点 $A=( a_{1} ,a_{2} ,\dotsc ,a_{n}) ,B( b_{1} ,b_{2} ,\dotsc ,b_{n})$ 間の距離は $\displaystyle d=\sum ^{n}_{i=1} |a_{i} -b_{i} |$ で表される。
#%% [markdown]
# ### Pythonでのマンハッタン距離の求め方
# ---
# `scipy.spatial.distance.cityblock`または`sklearn.metrics.pairwise.paired_manhattan_distances`を使用する。`paired_manhattan_distances`は入力に行列を想定しているので、ベクトル同士の距離の場合は $1\times 要素数$ の形にしてから実行する。

#%%
man = np.abs(a - b).sum()

#%%
help(cityblock)

#%%
np.isclose(man, cityblock(a, b))

#%%
help(paired_manhattan_distances)

#%%
np.isclose(man,
           paired_manhattan_distances(a.reshape((1, -1)), b.reshape((1, -1))))

#%% [markdown]
# ## コサイン類似度
# ---
# 2 つのベクトルの間の角度のコサインで、両ベクトルの類似度を表す。
# $
# \displaystyle \begin{aligned}
#     cos\theta  & =\frac
#         {a\cdot b}
#         {\| a\| \ \| b\| }
#     \\
#      & =\frac
#          {\displaystyle \sum ^{n}_{i=1} a_{i} b_{i}}
#          {\sqrt{
#              \displaystyle \sum ^{n}_{i=1} a^{2}_{i}
#          }\sqrt{
#              \displaystyle \sum ^{n}_{i=1} b^{2}_{i}
#          }}
# \end{aligned}
# $
# で表される。
#%% [markdown]
# ### Pythonでのコサイン類似度の求め方
# ---
# `scipy.spatial.distance.cosine`が $1-コサイン類似度$ なのでこれを利用するか、`sklearn.metrics.pairwise.cosine_similarity`を使用する。`cosine_similarity`は入力に行列を想定しているので、ベクトル同士の場合は $1\times 要素数$ の形にしてから実行する。

#%%
cos = a.dot(b) / np.sqrt(np.sum(a**2)) / np.sqrt(np.sum(b**2))

#%%
help(cosine)

#%%
np.isclose(cos, 1 - cosine(a, b))

#%%
help(cosine_similarity)

#%%
np.isclose(cos, cosine_similarity(a.reshape((1, -1)), b.reshape((1, -1))))
