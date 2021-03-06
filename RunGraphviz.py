print('generating graphviz diagram with graphviz for python')
from graphviz import Digraph
import yaml
import numpy as np
import doorstop
import textwrap
np.random.seed(0)
tree=doorstop.core.build()

dot = Digraph(comment='The Requirements', format='png')
dot.body.extend([ 'rankdir=LR','ratio=.8','size="300,300"','rank=min']) #,
dot.node_attr.update(color='lightblue2', style='filled',fontsize="30")

show_orphans=False
use_short_names=True
colors=['black','blue','chocolate','crimson', 'orchid', 'green','darkgreen','khaki','violet','purple','orange','lightblue2',]
n_colors = len(colors)

level_colors = ['gray95','gray88','gray79','darkgray68',]

for doc_n, document in  enumerate(tree.documents):

    #skip level 3:
    if doc_n >2:
        continue
    for i,item in enumerate(document.items):
        
        if use_short_names:
            content=item.uid.value+"\n"+str(item.data["..short name"])
        else:
            content=item.uid.value+"\n"+textwrap.fill(item.text,35)
        #skip items that have no back links, unless they are the first level
        if  show_orphans:
            dot.node(item.uid.value,content,color=level_colors[doc_n])#item.text)
        elif (len(item.links) >0) | (doc_n ==0):
            dot.node(item.uid.value,content,color=level_colors[doc_n])#item.text)
        else:
            print("skipping: "+item.uid.value)
            continue
        for link in item.links:
            width=str(np.random.rand()*5+5)
            if link.value[:6] ==item.uid.value[:6]:
                style='dashed'
            else:
                style='solid'
            dot.edge(link.value,item.uid.value,
                     color=colors[i % n_colors],
                     style=style,
                      penwidth=width)#, constraint='false')

dot.body.append('fontsize=20')
dot.render()#save("dot.svg")

print('graphviz rendered')
