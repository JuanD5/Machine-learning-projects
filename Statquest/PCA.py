#%%
import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA
from sklearn import  preprocessing
#from sklearn import StandardScaler
import matplotlib.pyplot as plt

#%%
genes = ['gene'+ str(i) for i in range(1,101)] # un array con 100 nombres de genomas 
print(genes)

wt = ['wt'+ str(i) for i in range(1,6)] # un array con 5 nombres de wild type 
print(wt)
ko = ['ko'+ str(i) for i in range(1,6)] # un array con 5 nombres de knock out 
print(ko)

#%% Se tienen 100 genes para 10 samples 
data = pd.DataFrame(columns=[*wt,*ko] ,index = genes) # las filas serán la expresión de los genes para esos dos samples 
for gene in data.index:
    data.loc[gene,'wt1':'wt5'] = np.random.poisson(lam = rd.randrange(10,1000),size = 5) # hacemos que se distribuyan según una poisson 
    data.loc[gene,'ko1':'ko5'] = np.random.poisson(lam = rd.randrange(10,1000),size = 5)
print(data.head())

#%% PCA 

scaled_data = preprocessing.scale(data.T)  # después de centrar los datos la media será 0 y la desviación estándar 1. Se pasa el dataset transpuesto porque se espera que los samples estén en forma de filas y no de columnas 
#scaled_data2 = StandardScaler().fit_transform(data.T) # otra forma de hacerlo 

pca = PCA()
pca.fit(scaled_data) # se obtienen los loading scores 
pca_data = pca.transform(scaled_data) # se generan las coordenadas  basandose en los scores y los datos escalados 

per_var = np.round(pca.explained_variance_ratio_*100,decimals=1)
labels = ['PC'+ str(x) for x in range(1,len(per_var)+1)]
plt.bar(x = range(1,len(per_var)+1),height= per_var , tick_label = labels)
plt.ylabel('Percentage of explained Variance')
plt.xlabel('Principal component')
plt.title('Screen plot')
plt.show()

pca_df = pd.DataFrame(pca_data,index=[*wt,*ko],columns = labels)
# rows : sample labels 
# columns : pc labels 
plt.scatter(pca_df.PC1, pca_df.PC2)
plt.title('PCA Graph')
plt.xlabel('PC1 - {0}%'.format(per_var[0]))
plt.ylabel('PC2 - {0}%'.format(per_var[1]))

for sample in pca_df.index:
    plt.annotate(sample,(pca_df.PC1.loc[sample],pca_df.PC2.loc[sample]))

plt.show()

# los K se muestran hacia la izquierda lo que sugiere que están relacionados entre si 
# los w se muestran a la derecha lo que sugiere que están relacionados entre si 

#%%
loading_scores = pd.Series(pca.components_[0],index= genes)
sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)
top_10_genes = sorted_loading_scores[0:10].index.values
print(loading_scores[top_10_genes])


