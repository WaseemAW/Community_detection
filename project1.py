import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from collections import defaultdict
import pandas as pd
#import community
#from scipy.cluster import hierarchy
#from scipy.spatial import distance
#from scipy.spatial.distance import pdist
#from scipy.cluster.hierarchy import linkage
#from sklearn.metrics.cluster import normalized_mutual_info_score
#from networkx.algorithms.community import greedy_modularity_communities
#from sklearn.cluster import AgglomerativeClustering
df1=pd.read_csv("Analysis_(v.2).csv",encoding = "ISO-8859-1")
p_a=df1['Name 1']
p_b=df1['Name 2']
df2=pd.concat([p_a,p_b],axis=0)    
df2_l=df2.values.tolist() # To count the frequency of names
# Filter vertices - each one must know 2 or more people
output = [] # Get unique values 
for x in p_a:
    if x not in output:
        output.append(x)
for x in p_b:
    if x not in output:
        output.append(x)
#print (output)
df3=pd.DataFrame(output)

p_a1=df1['Name 1'].values.tolist()
p_b1=df1['Name 2'].values.tolist()
output2 = [] # Get unique values again
for x in p_a1:
    if x not in output2:
        output2.append(x)
for x in p_b1:
    if x not in output2:
        output2.append(x)
      
# The number of viterces has been reduced from 232 to 89
## networkx - edgelist
l=list(zip(p_a1,p_b1)) # EDGELIST
NetxG1 = nx.Graph()
NetxG1.add_nodes_from(output2)
NetxG1.add_edges_from(l)
pos = nx.spring_layout(NetxG1)
plt.axis("off")

print("|||||||||||||||||||||||||||||||||||Divisive (Girvan-Newman Algorithms)||||||||||||||||||||||||||||||||||||||||||||||||")
comp1 =nx.algorithms.community.girvan_newman(NetxG1)
count =0
for Algo3 in comp1: 
    count= count+1
    if count == 2:
        A3=Algo3
        print("community")
        print (A3)

print("||||||||||||||||||||||||||||||||||Heirarchical link Clustering |||||||||||||||||||||||||||||||||||||||||||||||||")
preds = nx.jaccard_coefficient(NetxG1)
link = []
for LC in preds:

    link.append(LC[2])

for i in link:
    if i!=0:
        print(i)
nx.draw_networkx(NetxG1, pos = pos, cmap = plt.get_cmap("jet"), node_size = 350, with_labels = False)
plt.show()