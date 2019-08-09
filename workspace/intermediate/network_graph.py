#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'workspace/intermediate'))
    print(os.getcwd())
except:
    pass

#%%
import networkx as nx
from networkx.drawing.nx_pydot import to_pydot
from pydotplus import graph_from_dot_data
import matplotlib.pyplot as plt
from IPython.display import Image

#%% [markdown]
# ## Pythonでのネットワーク構造可視化
# ---
# SNS でのつながりのようなネットワークの可視化には`NetworkX`を使用する。
# グラフ (描画領域) ・ノード (基点) ・エッジ (ノードをつなぐ線) からなる。

#%%
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3, 4])
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 3)])
nx.draw(G)
plt.show()

#%% [markdown]
# ### 属性の付加
# ---
# エッジの属性`weight`はノード同士の近さで表現される。

#%%
G = nx.Graph(Network='My Network')
G.add_node(1, position='partner')
G.add_nodes_from([2, 3, 4], position='assistant')
G.add_edge(1, 2, weight=5, color='red')
G.add_edges_from([(1, 3), (1, 4)], weight=0.5)
G.add_edges_from([(2, 3, dict(weight=0.2)), (3, 4, dict(weight=0.3))])
nx.draw_networkx(G)
plt.show()

#%% [markdown]
# より多くの属性を指定して描画したい場合は[GraphViz](https://www.graphviz.org/)を利用して、[DOT言語](https://www.graphviz.org/doc/info/lang.html)形式で行う。

#%%
g = graph_from_dot_data(to_pydot(G).to_string())
Image(g.create_png())

#%% [markdown]
# ### 有向グラフ
# ---
# エッジに方向 (起点・終点) があるグラフ。

#%%
D = nx.DiGraph()
D.add_nodes_from([1, 2, 3, 4])
D.add_edge(1, 2, weight=5, color='red')
D.add_edges_from([(1, 3), (1, 4)], weight=0.5)
D.add_edges_from([(2, 3, dict(weight=0.2)), (3, 4, dict(weight=0.3))])
nx.draw_networkx(D)
plt.show()
