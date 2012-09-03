import json
import networkx as nx
from text_analysis import *

tweets = [ json.loads(s) for s in open('20120807150301.json', 'r').read().split('\n\n')[:-1]]

remove = 'Olympics #Olympics olympics #olympics'
remove = set(remove.split())

#lines = [ tweets['text'].encode('utf-8') for tweet in tweets[0][:]['text'] ]
lines = [ tweet['text'].encode('utf-8') for tweet  in tweets[0] ]

clean_lines = lines_cleanup( lines, 4, remove)
words = '\n'.join(clean_lines).split()

n_words = 15 
n_nodes = 15

wf = word_freq(words)

sorted_wf = sort_freqs(wf)

popular = sorted_wf[-n_nodes:]
pop_words = [wc[0] for wc in popular]
co_occur = co_occurrences(lines, pop_words)
cutoff = 10

wgraph = co_occurrences_graph(popular, co_occur, cutoff - 1)

wgraph = nx.connected_component_subgraphs(wgraph)[0]
centrality = nx.eigenvector_centrality_numpy(wgraph)

