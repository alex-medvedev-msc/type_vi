import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

def info_epsi_fixed (epsi):
	tab1 = pd.read_csv("/home/wintor/6_system/type_vi/2_stage/6_sys_genes.csv", ",")

	orgs = set(tab1.org_id.tolist())
	distances = []
	in_cluster = [] 
	for org in orgs:
		org_tab = tab1[(tab1.org_id == org)]
		org_tab.loc[:,["kegg_id", "start", "strand"]]
		X = org_tab.start.reshape(-1, 1) 
		db = DBSCAN(eps=epsi, min_samples=3).fit_predict(X)
		clustr_num = len(set(db)) - (1 if -1 in db else 0)
		print(org+" cluster num:", clustr_num)
		

		#colors = ['b', 'r', 'g', 'm', "w", "y", 'b', 'r', 'g', 'm', "w", "y"]
		#for i, j in zip(X, db):
		#	plt.scatter(i/1000, 1, c=colors[j+1])
			#print(i[0], j)
		#plt.show()

		print(org+" unic gene num:", len(set(org_tab.kegg_id)))
		print(org+" outside of cluster:", (db==-1).sum() )
		for clust in set(db):
			if clust==-1:
				continue
			elems = []

			for elem, cl in zip(X, db):
				if cl == clust:
					elems.append(elem[0])
			print(org, "cluster", clust)
			print(org, "distance", max(elems)-min(elems))
			distances.append(max(elems)-min(elems))
			in_cluster.append(len(elems))
		print()

	plt.hist(np.array(distances)/1000, bins=50)
	plt.show()

def main():
	info_epsi_fixed(20000)

if __name__ == '__main__':
	main()