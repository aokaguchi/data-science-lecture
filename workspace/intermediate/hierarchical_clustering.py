#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace/intermediate'))
    print(os.getcwd())
except:
    pass

#%% [markdown]
# ## 階層的クラスタリングの仕組み
# ---
# 1. 各サンプルをそれぞれ 1 つのクラスタとする
# 1. クラスタ内のある点を選び、別のクラスタの同様の点との間の距離を測る (クラスタ同士の全ての点の組み合わせを用いるものもある)
# 1. クラスタの全組み合わせの中から一番近いクラスタの組み合わせを選び、 1 つのクラスタとしてまとめる
# 1. 2~3 を指定した数のクラスタ数にまとめられるまで繰り返す
#
# <table class="text-center border">
#     <tr>
#         <th>距離の測り方 (metric)</th>
#     </tr>
#     <tr>
#         <td>ユークリッド距離<br />(euclidean)</td>
#     </tr>
#     <tr>
#         <td>マンハッタン距離<br />(cityblock)</td>
#     </tr>
#     <tr>
#         <td>その他<br /><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html">scipy.spatial.distance.pdist</a>を参照</td>
#     </tr>
# </table>
#
# <table class="text-center border">
#     <tr>
#         <th colspan="2">点の選び方 (method)</th>
#     </tr>
#     <tr>
#         <td>最短距離法・単リンク法<br />(single)</td>
#         <td class="text-left">クラスター同士で、最も近いサンプル同士</td>
#     </tr>
#     <tr>
#         <td>最長距離法・完全リンク法<br />(complete)</td>
#         <td class="text-left">クラスター同士で、最も遠いサンプル同士</td>
#     </tr>
#     <tr>
#         <td>群平均法・非加重結合法<br />(average)</td>
#         <td class="text-left">クラスター同士で、それぞれの要素すべての間 (の距離の平均)</td>
#     </tr>
#     <tr>
#         <td>重心法・セントロイド法<br />(centroid)</td>
#         <td class="text-left">クラスターの重心 (サンプル平均) 同士</td>
#     </tr>
#     <tr>
#         <td>ウォード法<br />(ward)</td>
#         <td class="text-left">統合前と統合後の散布度 (散らばり) の差 (後述)</td>
#     </tr>
#     <tr>
#         <td>その他</td>
#         <td class="text-left"><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html">scipy.cluster.hierarchy.linkage</a>を参照</td>
#     </tr>
# </table>
#
#

#%%
from helpers.hierarchical_clustering import algorithm
algorithm.show()

#%% [markdown]
# ## ウォード法
# ---
# ユークリッド距離の場合、クラスタAがサンプルサイズ $n$ 個・変数 $k$ 個 (データフレームなら、サイズが $n\times k$) のとき、クラスタAの重心 (クラスタ内の全サンプルの平均) からの各サンプルまでの距離の2乗の和 (各変数の変動の和) を $L( A) ={\displaystyle \sum ^{n}_{i=1}\sum ^{k}_{j=1}\left( x_{ij} -\overline{x}_{j}\right)^{2}}$ としたときに、情報ロス量 $\Delta =L( A\cup B) -L( A) -L( B)$ が最小となるようなクラスタA・Bから統合していく。 ( $A\cup B$ はA・Bを統合した後のクラスタ)
# イメージとしては、統合後の分散の増加を抑えるように統合していく。 (変動 = サンプルサイズ × 分散)
#%% [markdown]
# ## 注意点
# ---
# クラスタを統合するたびに、全ての組み合わせでクラスタ間距離を計算する必要があるため、サンプルサイズに対してスケールしにくい。
# 結果を可視化する際もサンプルサイズが大きいと何がどのクラスタに属しているのか確認しづらい。
