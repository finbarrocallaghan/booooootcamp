from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import subprocess as sp
from text_analysis import *
from cStringIO import StringIO
import json

filename = '20120807150601.json.gz'

unzipped_dirty = sp.check_output( [ 'zcat', filename ])

json_data = StringIO(unzipped_dirty.replace(']\n\n[',','))
tweets = json.load(json_data) 


geos = [ t['geo'] for t in tweets ]

m = Basemap(projection='robin',lon_0=0,resolution='c')
#set a background colour
m.drawmapboundary(fill_color='#85A6D9')
m.fillcontinents(color='white',lake_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawcountries(color='#6D5F47', linewidth=.4)
m.drawmeridians(np.arange(-180, 180, 30), color='#bbbbbb')
m.drawparallels(np.arange(-90, 90, 30), color='#bbbbbb')


lngs_lats = [ g.get('coordinates') for g in geos if g is not None] 
x,y = m(  [l[1] for l in lngs_lats]  ,  [l[0] for l in lngs_lats])

m.scatter(
    x,
    y,
    c='red', #color
    marker='o',
    alpha=0.75, #transparency
    zorder = 2, #plotting order
    )
