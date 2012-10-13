from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import subprocess as sp
from text_analysis import *
from cStringIO import StringIO
import json
import glob

filenames = glob.glob('201*') #independent of how many we fetched

unzipped_dirty = [sp.check_output( [ 'zcat', f ]) for f in filenames]

json_data = [StringIO(s.replace(']\n\n[',',')) for s in unzipped_dirty]

tweets = []
for j in json_data:
    try: tweets = tweets + json.load(j)
    except: pass

geos = [ t['geo'] for t in tweets ]

#m = Basemap(llcrnrlon=-100.,llcrnrlat=0.,urcrnrlon=-20.,urcrnrlat=57.,
            #projection='lcc',lat_1=20.,lat_2=40.,lon_0=-60.,
            #resolution ='l',area_thresh=1000.)

m = Basemap(llcrnrlon=-10.,llcrnrlat=20,urcrnrlon=55.,urcrnrlat=75,\
            resolution='l',projection='aea',\
            lat_1=40.,lat_2=60,lon_0=35.)



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
