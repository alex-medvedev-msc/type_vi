import seaborn as sns
import numpy as np
import pandas as pd

tab1 = pd.read_csv("/home/wintor/6_system/type_vi/2_stage/6_sys_genes.csv", ",")
for i, row in tab1.iterrows():

x = np.random.normal(size=1000)

sns.distplot(x)

mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])
sns.jointplot(x="x", y="y", data=df);




sns.plt.show()