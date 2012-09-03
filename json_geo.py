import subprocess as sp
from cStringIO import StringIO
import json
import glob

#filename = '20120807150601.json.gz'
# filenames =['20120807150301.json.gz',
# 	    '20120807150601.json.gz',
# 	    '20120807150901.json.gz',
# 	    '20120807151201.json.gz',
# 	    '20120807151501.json.gz',
# 	    '20120807151734.json.gz',
# 	    '20120807151958.json.gz',
# 	    '20120807152202.json.gz',
# 	    '20120807152302.json.gz',
# 	    '20120807152401.json.gz',
# 	    '20120807152502.json.gz',
# 	    '20120807152601.json.gz',
# 	    '20120807152701.json.gz',
# 	    '20120807152801.json.gz',
# 	    '20120807154101.json.gz',
# 	    '20120807154201.json.gz',
# 	    '20120807154301.json.gz',
# 	    '20120807154402.json.gz',
# 	    '20120807154501.json.gz',
# 	    '20120807154601.json.gz',
# 	    '20120807154702.json.gz',
# 	    '20120807154801.json.gz',
# 	    '20120807154901.json.gz',
# 	    '20120807155001.json.gz',
# 	    '20120807155101.json.gz',
# 	    '20120807155201.json.gz',
# 	    '20120807155302.json.gz',
# 	    '20120807155402.json.gz',
# 	    '20120807155501.json.gz',
# 	    '20120807155601.json.gz',
# 	    '20120807155701.json.gz',
# 	    '20120807155801.json.gz',
# 	    '20120807155902.json.gz',
# 	    '20120807160002.json.gz',
# 	    '20120807160101.json.gz']
filenames = glob.glob('201*') #independent of how many we fetched

unzipped_dirty = [sp.check_output( [ 'zcat', f ]) for f in filenames]
#unzipped_dirty = reduce(str.__add__, unzipped_dirty)

json_data = [StringIO(s.replace(']\n\n[',',')) for s in unzipped_dirty]

tweets = []
for j in json_data:
    try: tweets = tweets + json.load(j)
    except: pass

#tweets = [json.load(j) for j in json_data]
#tweets = reduce(list.__add__, tweets) 

geos = [ t['geo'] for t in tweets ]

lngs_lats = [ g.get('coordinates') for g in geos if g is not None] 

