import pandas as pd
import numpy as np
from sets import Set
data = pd.read_csv('HighLevelTicketLocationData_1.csv')

print data.columns

print data.shape

category_counter = {}

categories = data['RESOLUTION_CATEGORY']
types = data['RESOLUTION_TYPE']

for i in xrange(len(categories)):
    category = categories[i]
    t = types[i]
    if category in category_counter:
        category_counter[category].add(t)
    else:
        category_counter[category] = set([t])

del category_counter[np.nan]

print len(category_counter)

print category_counter

#from scipy import sttas
#import scipy.stats


#from scipy.stats import ttest_ind

#stats.scipy.ttest_ind(data['EQ_MARKET'],data['RESOLUTION_CATEGORY'])

#print np.unique(data['RESOLUTION_CATEGORY'])
