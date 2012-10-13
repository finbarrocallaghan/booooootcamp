#import pandas
#import pylab as py

#athletes = pandas.read_csv('London2012athletes.csv')



from datetime import datetime                                                                    
import pylab as py                                                                               
import pandas                                                                                    
import fuzzy                                                                                     
                                                                                                 
parse = lambda x : datetime.strptime(x, '%d/%m/%Y %H:%M')                                        
it = pandas.read_csv('closed_it.csv', parse_dates=[[1,2]], index_col=0,date_parser=parse)        
                                                                                                 
                                                                                                 
duplicates = {}                                                                                  
jobcounts = {}                                                                                   
                                                                                                 
for tstamp,user in it.Requested_By.iteritems():                                                  
  if ',' in user:                                                                                
    user = ' '.join(user.split(',')[::-1])                                                       
                                                                                                 
  if  user in duplicates :                                                                       
    user = duplicates[user]                                                                      
  if user not in jobcounts :                                                                     
    jobcounts[user] =  [tstamp.to_pydatetime()]                                                  
  else :                                                                                         
    jobcounts[user].append(tstamp.to_pydatetime())                                               
                                                                                                 
jobcounts = sorted( jobcounts.items(),                                                           
                    key= lambda item : len(item[1]),reverse=True)                                
                                                                                                 
user_list = [ x for x,y in jobcounts ]                                                           
                                                                                                 
users_to_plot = 20                                                                               
                                                                                                 
py.figure(1,figsize=(10.45,12.2875))                                                             
for user, date_list in  jobcounts[:users_to_plot]:                                               
  #py.subplot(211)                                                                               
  dates  = sorted(date_list)                                                                     
  requests= py.arange(1, len(date_list)+1)                                                       
  py.plot(dates , requests,label='{0},{1}'.format(requests[-1], user) )                          
  ax = py.gca()                                                                                  
  a= ax.get_lines()                                                                              
  py.plot(dates[-1],requests[-1],'o',c=a[-1].get_color() , ms=5)                                 
  py.plot(dates[0],requests[0],'o',c=a[-1].get_color() , ms=5)                                   
                                                                                                 
handles, labels= ax.get_legend_handles_labels()                                                  
#py.legend([x[0] for x in jobcounts[:users_to_plot]], loc = 'upper left', prop={'size':15} )     
py.legend( loc = 'upper left', prop={'size':15} )                                                
py.grid(True)                                                                                    
                                                                                                 
with open('file.txt', 'w') as file:                                                              
  for item in labels :                                                                           
    file.write("{}\n".format(item))                                                              
                                                                                                 
                                                                                                 
  #py.subplot(212)                                                                               
  #py.plot(sorted(date_list), py.arange(1, len(date_list)+1))                                    
                                                                                                 
#py.subplot(212)                                                                                 
#py.grid(True)                                                                                   
                                                                                                 
#py.subplot(211)                                                                                 


from pylab import *                                                                                                      
                                                                                                                         
from mpl_toolkits.basemap import Basemap                                                                                 
import pandas                                                                                                            
import shapefile                                                                                                         
from matplotlib.patches import Polygon                                                                                   
from matplotlib import cm                                                                                                
from datetime import datetime                                                                                            
                                                                                                                         
import matplotlib.colors as c                                                                                            
                                                                                                                         
parse = lambda x : datetime.strptime(x, '%d/%m/%Y')                                                                      
houses12 = pandas.read_csv('PPR_2012.csv',parse_dates=[0],date_parser=parse,thousands=',')#,encoding='utf-8')            
                                                                                                                         
cc = houses12.groupby('county')                                                                                          
                                                                                                                         
number_of_houses = { x:sqrt(float(y)/cc.size().max()) for  x,y in cc.size().iteritems() }                                
                                                                                                                         
                                                                                                                         
#number_of_houses =  c.LogNorm( cc.size() )                                                                              
                                                                                                                         
prices = cc['price']                                                                                                     
analyze  = prices.var()                                                                                                  
                                                                                                                         
                                                                                                                         
total_price = { x:sqrt(float(y)/analyze.max()) for x,y in analyze.iteritems() }                                          
                                                                                                                         
                                                                                                                         
#by_date = houses12.groupby(['county','date_of_sale'])['price'].sum()                                                    
#by_date.unstack('county').cumsum().plot()                                                                               
                                                                                                                         
                                                                                                                         
                                                                                                                         
figure(1,figsize=(11.7,8.3))                                                                                             
ax = subplot(111)                                                                                                        
                                                                                                                         
m = Basemap(llcrnrlon=-11.,llcrnrlat=50.5,urcrnrlon=-5.,urcrnrlat=56.,                                                   
            resolution='i',area_thresh=1000.,projection='tmerc',lon_0=-8.,lat_0=0.)                                      
                                                                                                                         
irl = m.readshapefile('IRL_adm0','country',color='#6D5F47',linewidth=0.05)                                               
shp_info = m.readshapefile('IRL_adm1','counties', color='#6D5F47',linewidth=0.2)                                         
                                                                                                                         
for nshape, seg in enumerate(m.counties):                                                                                
  cname =  m.counties_info[nshape]['NAME_1']                                                                             
  if cname == 'Laoighis':                                                                                                
    cname = 'Laois'                                                                                                      
                                                                                                                         
  poly = Polygon(seg, facecolor= cm.Reds(number_of_houses[cname]))                                                       
  ax.add_patch(poly)                                                                                                     
                                                                                                                         


