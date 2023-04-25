import pandas as pd
import warnings
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

dataset = pd.read_csv('tweets.csv')
dataset = dataset[dataset.user_location.notnull()][:10]
dataset['hashtags'] = ''

for i, row in dataset.iterrows():
    hashtags = [token for token in row.tweet.split() if token.startswith('#')]
    dataset['hashtags'][i] = hashtags

dataset = dataset.explode('hashtags')
users = list(dataset['user'].unique())
hashtags = list(dataset['hashtags'].unique())

vis = nx.Graph()
vis.add_nodes_from(users + hashtags)

for name, group in dataset.groupby(['hashtags', 'user']):
    hashtag, user = name
    weight = len(group)
    vis.add_edge(hashtag, user, weight=weight)


# Community Detection
community_gen = community.girvan_newman(vis)
top_level_communities = next(community_gen)

communities = list(next(community_gen))
print("Comm", communities)
# colors = ['red', 'yellow', 'orange']
# node_colors = {}

# for i, comm in enumerate(communities):
#     for node in comm:
#         node_colors[node] = colors[i]

# nx.set_node_attributes(vis, node_colors, name='color')
# node_colors = nx.get_node_attributes(vis, 'color')

nx.draw(vis)
plt.axis('off')
plt.show()


# Influential Node Analysis
centrality = nx.betweenness_centrality(vis)
print('Top 5 Most Influential Users/Hashtags based on betweenness centrality :- ')
influential_nodes = sorted(
    centrality.items(), key=lambda item: item[1], reverse=True)[:5]

for nodes in influential_nodes:
    print(f'{nodes[0]} : {nodes[1]}')
