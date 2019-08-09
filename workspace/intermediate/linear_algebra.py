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
import seaborn as sns
from IPython.display import display
pd.set_option('max_rows', 5)

#%% [markdown]
# ## ベクトルと行列
# ---
# 数値の並んだ一次元配列のことをベクトルといい、横方向に並んだものを横ベクトルや行ベクトル、縦方向に並んだものを縦ベクトルや列ベクトルと呼ぶ。
#
# 横ベクトル・行ベクトル $( 1 \ 2 \ \dots \ n)$
#
# 縦ベクトル・列ベクトル $
# \left(
#     \begin{array}{ c }
#         1\\
#         2\\
#         \vdots \\
#         n
#     \end{array}
# \right)
# $
#
# 数値の並んだ二次元配列のことを行列と呼ぶ。行列の各行・各列は同じ要素数でなければならず、空きがあってはいけない。
#
# 行列 $
# \left(
#     \begin{array}{ c c c }
#         1 & 2 & 3\\
#         4 & 5 & 6
#     \end{array}
# \right)
# $
#%% [markdown]
# ## ベクトルと行列の転置
# ---
# 横ベクトルを縦ベクトル、またはその逆にしたり、行列の行と列を入れ替える操作を転置といい、以下のように表す。
#
# $
# ( 1,2,3)^{T} =\begin{pmatrix}
#     1\\
#     2\\
#     3
# \end{pmatrix} ,\begin{pmatrix}
#     1 & 2 & 3\\
#     4 & 5 & 6
# \end{pmatrix}^{T} =\begin{pmatrix}
#     1 & 4\\
#     2 & 5\\
#     3 & 6
# \end{pmatrix}
# $
#%% [markdown]
# ### Pythonでの転置の実行方法
# ---
# ベクトルは基本的に横ベクトルとして扱われるが、ブロードキャストという機能によって自動的に縦ベクトルに変換されたかのような挙動をすることもある。明示的に縦ベクトルにするには列数1の行列に`reshape`する。
# 行列は`T`属性で転置行列が得られる。

#%%
a = np.arange(6).reshape((2, 3))
a

#%%
a.T

#%% [markdown]
# ## ベクトルの内積
# ---
# ベクトルや行列を掛ける場合、一定のルールがある。(内積と呼ばれる)
#
# ベクトル同士を掛ける場合は、次元(要素数)が同じでなければならない。演算子も $\times$ ではなく $\cdot$ を使用する。
#
# $a=( a_{1} \ a_{2} \ \dots \ a_{n}) ,\ b=( b_{1} \ b_{2} \ \dots \ b_{n})$ の場合、 $ab=a_{1} b_{1} +a_{2} b_{2} +\dots +a_{n} b_{n}$
#
# 具体例：$( 1\ 2\ 3) \cdot ( 4\ 5\ 6) =1\times 4+2\times 5+3\times 6=32$

#%%
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

#%% [markdown]
# ###### 練習問題
# ベクトル $a$ と $b$ の内積を求める。 (NumPy の関数は使用しない)

#%%

#%% [markdown]
# ### Pythonでの内積の実行方法
# ---
# `numpy.dot`または`@`演算子を使用する。

#%%
help(np.dot)

#%%
a.dot(b)

#%%
np.dot(a, b)

#%%
a @ b

#%% [markdown]
# ## 行列の内積
# ---
# 行列同士の内積は掛ける順番にも意味がある。行列の内積の場合には、行ベクトル $\times$ 列ベクトルの順番でかけると計算結果は、それぞれのベクトルの同じ順番の要素同士を掛けたものの和になる。そして、以下のように計算する。
#
# $i$ 行 $j$ 列の行列 $A$ と$j$ 行 $k$ 列の行列 $B$ を考える。
#
# $
# A=\left(
#     \begin{array}{ c c c c }
#         a_{11} & a_{12} & \dots  & a_{1j}\\
#         a_{21} & a_{22} & \dots  & a_{2j}\\
#         \vdots  & \vdots  & \ddots  & \vdots \\
#         a_{i1} & a_{i2} & \dots  & a_{ij}
#     \end{array}
# \right) ,\ B=\left(
#     \begin{array}{ c c c c }
#         b_{11} & b_{12} & \dots  & b_{1k}\\
#         b_{21} & b_{22} & \dots  & b_{2k}\\
#         \vdots  & \vdots  & \ddots  & \vdots \\
#         b_{j1} & b_{j2} & \dots  & b_{jk}
#     \end{array}
# \right)
# $
#
# $A$ ・ $B$ をそれぞれ行ベクトル $a$ ・列ベクトル $b$ の集合とする。
#
# $
# \begin{cases}
#     a_{1} =( a_{11} \ a_{12} \ \dots \ a_{1j})\\
#     a_{2} =( a_{21} \ a_{22} \ \dots \ a_{2j})\\
#     \vdots \\
#     a_{i} =( a_{i1} \ a_{i2} \ \dots \ a_{ij})
# \end{cases} ,\ A=\left(
#     \begin{array}{ c }
#         a_{1}\\
#         a_{2}\\
#         \vdots \\
#         a_{i}
#     \end{array}
# \right)
# $
#
# $
# b_{1} =\left(
#     \begin{array}{ c }
#         b_{11}\\
#         b_{21}\\
#         \vdots \\
#         b_{j1}
#     \end{array}
# \right) ,\ b_{2} =\left(
#     \begin{array}{ c }
#         b_{12}\\
#         b_{22}\\
#         \vdots \\
#         b_{j2}
#     \end{array}
# \right) ,\ \dots ,\ b_{k} =\left(
#     \begin{array}{ c }
#         b_{1k}\\
#         b_{2k}\\
#         \vdots \\
#         b_{jk}
#     \end{array}
# \right) ,\ B=( b_{1} \ b_{2} \ \dots \ b_{k})
# $
#
# 内積 $AB$ は以下で求められる。
#
# $
# AB=\left(
#     \begin{array}{ c c c c }
#         a_{1} b_{1} & a_{1} b_{2} & \dots  & a_{1} b_{k}\\
#         a_{2} b_{1} & a_{2} b_{2} & \dots  & a_{2} b_{k}\\
#         \vdots  & \vdots  & \ddots  & \vdots \\
#         a_{i} b_{1} & a_{i} b_{2} & \dots  & a_{i} b_{k}
#     \end{array}
# \right)
# $
#
# 具体例：
#
# $
# \begin{align}
#     \left(
#         \begin{array}{ c c }
#             1 & 2\\
#             3 & 4\\
#             5 & 6
#         \end{array}
#     \right) \cdot \left(
#         \begin{array}{ c c c c }
#             7 & 8 & 9 & 10\\
#             11 & 12 & 13 & 14
#         \end{array}
#     \right) & =\left(
#         \begin{array}{ c }
#             ( 1\ 2)\\
#             ( 3\ 4)\\
#             ( 5\ 6)
#         \end{array}
#     \right) \cdot \left(
#         \begin{array}{ c c c c }
#             \left(
#                 \begin{array}{ c }
#                     7\\
#                     11
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c }
#                     8\\
#                     12
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c }
#                     9\\
#                     13
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c }
#                     10\\
#                     14
#                 \end{array}
#             \right)
#         \end{array}
#     \right)\\
#      & =\left(
#          \begin{array}{ c c c c }
#             \left(
#                 \begin{array}{ c c }
#                     1 & 2
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     7\\
#                     11
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c c }
#                     1 & 2
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     8\\
#                     12
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c c }
#                     1 & 2
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     9\\
#                     13
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c c }
#                     1 & 2
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     10\\
#                     14
#                 \end{array}
#             \right)\\
#             \left(
#                 \begin{array}{ c c }
#                     3 & 4
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     7\\
#                     11
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c c }
#                     3 & 4
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     8\\
#                     12
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c c }
#                     3 & 4
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     9\\
#                     13
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c c }
#                     3 & 4
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     10\\
#                     14
#                 \end{array}
#             \right)\\
#             \left(
#                 \begin{array}{ c c }
#                     5 & 6
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     7\\
#                     11
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c c }
#                     5 & 6
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     8\\
#                     12
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c c }
#                     5 & 6
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     9\\
#                     13
#                 \end{array}
#             \right) & \left(
#                 \begin{array}{ c c }
#                     5 & 6
#                 \end{array}
#             \right) \cdot \left(
#                 \begin{array}{ c }
#                     10\\
#                     14
#                 \end{array}
#             \right)
#         \end{array}
#     \right)\\
#      & =\left(
#          \begin{array}{ c c c c }
#             1\times 7+2\times 11 & 1\times 8+2\times 12 & 1\times 9+2\times 13 & 1\times 10+2\times 14\\
#             3\times 7+4\times 11 & 3\times 8+4\times 12 & 3\times 9+4\times 13 & 3\times 10+4\times 14\\
#             5\times 7+6\times 11 & 5\times 8+6\times 12 & 5\times 9+6\times 13 & 5\times 10+6\times 14
#         \end{array}
#     \right)\\
#      & =\left(
#          \begin{array}{ c c c c }
#             29 & 32 & 35 & 38\\
#             65 & 72 & 79 & 86\\
#             101 & 112 & 123 & 134
#         \end{array}
#     \right)
# \end{align}
# $
#%% [markdown]
# ###### 練習問題
#
# 行列 $A$ ・ $B$ の内積 $AB$ を求める関数`dot`を完成させる。

#%%
i, j, k = 3, 4, 5
np.random.seed(1234)
A = np.random.choice(range(1, 10), size=(i, j))
B = np.random.choice(range(1, 10), size=(j, k))
print('A=')
print(A)
print('B=')
print(B)


#%%
def dot(A, B):
    # 出力のサイズを決定する
    out_size = (__, __)

    AB = np.empty(out_size)
    for (r, c), _ in np.ndenumerate(AB):
        # 出力のr行c列の要素を計算して代入する
        AB[r, c] = __
    return AB


#%%
dot(A, B)

#%% [markdown]
# ###### 練習問題
#
# 全ての要素が 1 である 5x3 行列と 3x2 行列の内積を求める ([100 numpy exercises #24](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb))
#%% [markdown]
# ベクトルと行列をかける場合は、行ベクトルを行数1の行列、列ベクトルを列数1の行列と考えて、行列同士の場合と同じように行う。
#
# 慣れないうちは行列のサイズのみに注目し、 $( M\times K) \cdot ( K\times N) =( M\times N)$ のように内側の数を揃えることと、出力のサイズが外側をつなげたものになることだけ覚えておくとよい。
#%% [markdown]
# ### Pythonでの実行方法
# ---
# ベクトルの内積と同様に`numpy.dot`や`@`を使用する。

#%%
A.dot(B)

#%%
np.dot(A, B)

#%%
A @ B

#%%
a.dot(A)

#%% [markdown]
# ### 数式での表記とプログラミングの違い
# ---
# 以降の数式ではベクトルは縦ベクトル (列ベクトル) を基本とする。例えば、ある人の身長・体重などを表すデータ (ベクトル) は $
# \begin{pmatrix}
#     170cm\\
#     60kg\\
#     \vdots
# \end{pmatrix}
# $ となる。複数人のデータの場合は $
# \begin{pmatrix}
#     170cm & 180cm & \cdots \\
#     60kg & 70kg & \cdots \\
#     \vdots  & \vdots  & \ddots
# \end{pmatrix}
# $ のようになる。これは実際に扱うデータやプログラムとは行と列が逆になっているので、特に内積の計算で数式とプログラムの記述の違いに早く慣れておく。
# 慣れないうちは、上にあるように行列の形を考える。
#%% [markdown]
# ###### 練習問題
#
# `iris`データセットを $X$ (4行×サンプルサイズ) とした場合に $y=aX$ ($y$ は2×サンプルサイズの行列) となるような $a$ の形を考える。
# 実際にプログラムで $a$ (中身は任意) を作成し、実行する。ただし、結果はサンプルサイズ×2列の行列になるようにする。

#%%
iris = sns.load_dataset('iris').iloc[:, :4]
print('iris')
display(iris)

#%%
