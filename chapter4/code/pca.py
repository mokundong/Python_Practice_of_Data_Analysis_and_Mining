import pandas as pd
inputfile = '../data/principal_component.xls'
outputfile = '../tmp/dimention_reducted.xls'

data = pd.read_excel(inputfile)

from sklearn.decomposition import PCA
# pca = PCA()
# pca.fit(data)
# print(pca.components_)
# print(pca.explained_variance_ratio_)

pca = PCA(3)
pca.fit(data)
low_d = pca.transform(data)
pd.DataFrame(low_d).to_excel(outputfile)
pca.inverse_transform(low_d)