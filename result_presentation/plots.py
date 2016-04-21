import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as pt

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler


tab1 = pd.read_csv("/home/wintor/6_system/type_vi/2_stage/6_sys_genes.csv", ",")



eko1 = tab1[(tab1.org_id == "eko")&(tab1.strand==-1)]
eko1.loc[:,["kegg_id", "start", "strand"]]

eko2 = tab1[(tab1.org_id == "eko")&(tab1.strand==1)]
eko2.loc[:,["kegg_id", "start", "strand"]]


'''
f, p = pt.subplots(2, sharex=True)


x1 = range(len(eko1.start))
x2 = range(len(eko1.start), len(eko1.start)+len(eko2.start))

p[0].plot(x1, eko1.start, 'ro')

for label, x, y in zip(eko1.kegg_id, x1, eko1.start):
	p[0].annotate(label, (x, y))


p[1].plot(x2, eko2.start, 'ro')

for label, x, y in zip(eko2.kegg_id, x2, eko2.start):
	p[1].annotate(label, (x, y))
'''





#f, p = pt.subplots(2, sharex=True)

x1 = [1 for i in eko1.start]
x2 = [1 for i in eko2.start] 

y1 = eko1.start
y2 = eko2.start

'''
p[0].plot(y1, x1, 'ro')

for label, x, y in zip(eko1.kegg_id, y1, x1):
	p[0].annotate(label, (x, y))


p[1].plot(y2, x2, 'ro')

for label, x, y in zip(eko2.kegg_id, y2, x2):
	p[1].annotate(label, (x, y))
'''

X = y1.reshape(-1, 1)

db = DBSCAN(eps=100000, min_samples=3).fit_predict(X)
ma = max(db)+1
colors = ['b', 'r', 'g', 'm']

for i, j in zip(X, db):
	pt.scatter(i, 1, c=colors[j+1])
	print(i[0], j)

pt.show()
