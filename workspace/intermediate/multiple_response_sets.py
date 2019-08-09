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
import seaborn as sns
from IPython.display import display
pd.set_option('max_rows', 7)

#%% [markdown]
# ## 多重クロス集計
# ---
# 3 変数以上をまとめたクロス集計表。習熟すれば得られる情報は多くなるが、慣れないとかえってわかりにくい。

#%%
titanic = sns.load_dataset('titanic')
print('titanic')
display(titanic)

#%% [markdown]
# ### Pythonでの多重クロス集計実行方法
# ---
# `pandas.crosstab`の`index`または`columns`に複合インデックスにしたいデータをリストで渡す。

#%%
help(pd.crosstab)

#%%
pd.crosstab(index=[titanic['class'], titanic['sex']],
            columns=titanic['embark_town'])
