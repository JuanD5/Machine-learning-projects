#%%
from sklearn.datasets import  make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt 

#%%
X, y = make_classification(n_samples=1000, n_classes=2, n_features=20, random_state=27)
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3, random_state=27)
#%%
model1 = LogisticRegression()
model2 = KNeighborsClassifier(n_neighbors=4)
model1.fit(X_train, y_train)
model2.fit(X_train, y_train)
pred_prob1 = model1.predict_proba(X_test) # se obtiene la probabilidad de que pertenezca tanto a la clase 0  como a la clase 1 
pred_prob2 = model2.predict_proba(X_test)

print(pred_prob1[:,1])# todas las filas, primera columna 
#%%

# En este paso se compara con las anotaciones o labels de test 
fpr1, tpr1, thresh1 = roc_curve(y_test, pred_prob1[:,1], pos_label=1)
fpr2, tpr2, thresh2 = roc_curve(y_test, pred_prob2[:,1], pos_label=1)

# roc curve for tpr = fpr 
random_probs = [0 for i in range(len(y_test))]
p_fpr, p_tpr, _ = roc_curve(y_test, random_probs, pos_label=1)

auc_score1 = roc_auc_score(y_test, pred_prob1[:,1])
auc_score2 = roc_auc_score(y_test, pred_prob2[:,1])
print(auc_score1, auc_score2)

plt.style.use('seaborn')

# plot roc curves
plt.plot(fpr1, tpr1, linestyle='--',color='orange', label='Logistic Regression')
plt.plot(fpr2, tpr2, linestyle='--',color='green', label='KNN')
plt.plot(p_fpr, p_tpr, linestyle='--', color='blue')
# title
plt.title('ROC curve')
# x label
plt.xlabel('False Positive Rate')
# y label
plt.ylabel('True Positive rate')

plt.legend(loc='best')
plt.savefig('ROC',dpi=300)
plt.show();