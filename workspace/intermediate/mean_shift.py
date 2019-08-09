#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace/intermediate'))
    print(os.getcwd())
except:
    pass

#%% [markdown]
# ## Mean Shiftの仕組み
# ---
# 特徴空間で、指定した距離内の密度が最大化するようにクラスタ中心を決める手法。
# 1. 初期のクラスタ中心を選ぶ
#  - 全てのサンプルをクラスタ中心に選ぶ
#  - 格子状に領域を分割し、一定以上のサンプル数が含まれる区間をクラスタ中心に選ぶ
# 1. 指定された距離内のデータ点を元に密度が最大になる方向 (指定範囲内のサンプル重心 = 平均) にクラスタ中心を移動する
# 1. 収束するまで 2 を繰り返す
# 1. 指定された距離内にクラスタ中心が複数ある場合には密度の高いものを残す

#%%
from helpers.mean_shift import algorithm
algorithm.show()

#%% [markdown]
# ## 注意点
# ---
# Mean Shift は、指定した距離内にサンプルがあるか確かめるため、クラスタ中心から全サンプルまでの距離を計算する必要があるため、サンプルサイズに対してスケールしにくい。
