#!/usr/bin/env python
import networkx as nx
import subprocess as sp
from text_analysis import *
from cStringIO import StringIO
import json

import fileinput

for filename in fileinput.input():
   pass

#filename = '20120807150601.json.gz'

unzipped_dirty = sp.check_output( [ 'zcat', filename.split('\n')[0] ])
json_data = StringIO(unzipped_dirty.replace(']\n\n[',','))
tweets = json.load(json_data) 


remove = ( 'this that your with have watch #olympics should'
           'being olympics olympic' )

remove = set(remove.split())

#lines = [ t['text'].encode('utf-8') for t in tweets ]
lines = [ t['text'] for t in tweets ]

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
summarize_freq_hist(wf)
summarize_centrality(centrality)


