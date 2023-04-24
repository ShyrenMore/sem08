import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community
from networkx.algorithms.link_analysis import pagerank

# Read in Excel file
# df = pd.read_excel('NBA.xlsx')
df = pd.read_csv('community.csv')

# Create empty graph
G = nx.Graph()
demodf = df.head(20)

# Iterate over rows and add edges to graph
for idx, row in demodf.iterrows():
    postid = row['PostCode']
    tagged = row['Mentions']
    if pd.isna(tagged):
        continue
    for tag in tagged.split(','):
        G.add_edge("post:"+postid, tag.strip())

# Set spring layout algorithm to position nodes
pos = nx.spring_layout(G, k=0.75)

# Plot graph with labels
nx.draw(G, pos=pos, with_labels=True)

# Draw edges
nx.draw_networkx_edges(G, pos=pos, alpha=0.5)

# Set node labels
node_labels = {n: n for n in G.nodes()}

# Draw node labels
nx.draw_networkx_labels(G, pos=pos, labels=node_labels)

# Show graph
plt.show()

shortdf = df.head(20)
len(shortdf)

#community detection using girvan newman
# Create empty graph
G = nx.Graph()

# Iterate over rows and add edges to graph
for idx, row in shortdf.iterrows():
    postid = row['PostCode']
    tagged = row['Mentions']
    if pd.isna(tagged):
        continue
    for tag in tagged.split(','):
        G.add_edge("post:"+postid, tag.strip())

communities_generator = community.girvan_newman(G)
communities = next(communities_generator)

# Print communities in human-readable format
print("Communities:")
for i, com in enumerate(communities):
    print(f"Community {i+1}: {', '.join(sorted(com))}")

# Create a color map for each community
color_map = {}
for i, c in enumerate(communities):
    for n in c:
        color_map[n] = i

# Set spring layout algorithm to position nodes
pos = nx.spring_layout(G, k=1)

# Plot graph with labels and node colors
nx.draw(G, pos=pos, with_labels=True, node_color=[
        color_map[n] for n in G.nodes()])

# Draw edges
nx.draw_networkx_edges(G, pos=pos, alpha=0.5)

# Set node labels
node_labels = {n: n for n in G.nodes()}

# Draw node labels
nx.draw_networkx_labels(G, pos=pos, labels=node_labels)

# Show graph
plt.show()
