# -*- coding: utf-8 -*-
"""Support_Vector_Machine_Astrocytoma


Automatically generated by Colaboratory.


Original file is located at
   https://colab.research.google.com/drive/1D6eHKEyUG_SnlYy3C-wne0RdctvCAaXa
"""


# Commented out IPython magic to ensure Python compatibility.
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for statistical data visualization
# %matplotlib inline


metadata = pd.read_csv('interesting_metadata_for_astrocytoma_vs_normal.csv')
metadata = metadata[["Unnamed: 0", "disease:ch1"]]
metadata.rename(columns={'Unnamed: 0':'sample_name'}, inplace=True)
metadata = metadata.set_index('sample_name', drop=False).rename_axis(None)
metadata = metadata.iloc[: , 1:]
metadata["disease:ch1"].value_counts()


df = pd.read_csv('interesting_genes_expressions_for_astrocytoma_vs_normal.csv')
df.rename(columns={'Unnamed: 0':'probe_id'}, inplace=True)
df_transposed = df.T
df_transposed = df_transposed.rename(columns=df_transposed.iloc[0])
df_transposed.drop(index=df_transposed.index[0], axis=0, inplace=True)


frames = [metadata, df_transposed]
df = pd.concat(frames, axis=1)
df['disease:ch1'] = pd.factorize(df['disease:ch1'])[0]


for i in range(1, len(df.columns)):
   df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], errors='ignore')


df.describe() # Description of statistic features (Sum, Average, Variance, minimum, 1st quartile, 2nd quartile, 3rd Quartile and Maximum)


# view the percentage distribution of target_class column
df['disease:ch1'].value_counts()/np.float(len(df))


# view summary of dataset
df.info()


# view summary statistics in numerical variables
round(df.describe(),2)


df_astrocytoma = df[df['disease:ch1'] == 0]
plt.figure(figsize=(15,10))
plt.scatter(df_astrocytoma['241672_at'], df_astrocytoma['237509_at'])
plt.title('Scatter plot gene expression')
plt.xlabel('SERTM1')
plt.ylabel('LINC01616')
plt.show()


col_names = df.columns


# check distribution of target_class column
df['disease:ch1'].value_counts()
df.reset_index(inplace=True)
df_corr = df.corr()


# draw boxplots to visualize outliers


plt.figure(figsize=(24,20))


plt.subplot(4, 2, 1)
fig = df.boxplot(column='241672_at')
fig.set_title('')
fig.set_ylabel('241672_at')


plt.subplot(4, 2, 2)
fig = df.boxplot(column='237509_at')
fig.set_title('')
fig.set_ylabel('237509_at')


plt.subplot(4, 2, 3)
fig = df.boxplot(column='220030_at')
fig.set_title('')
fig.set_ylabel('220030_at')


plt.subplot(4, 2, 4)
fig = df.boxplot(column='230765_at')
fig.set_title('')
fig.set_ylabel('230765_at')


plt.subplot(4, 2, 5)
fig = df.boxplot(column='1556366_s_at')
fig.set_title('')
fig.set_ylabel('1556366_s_at')


plt.subplot(4, 2, 6)
fig = df.boxplot(column='215531_s_at')
fig.set_title('')
fig.set_ylabel('215531_s_at')


plt.subplot(4, 2, 7)
fig = df.boxplot(column='240512_x_at')
fig.set_title('')
fig.set_ylabel('240512_x_at')


plt.subplot(4, 2, 8)
fig = df.boxplot(column='206084_at')
fig.set_title('')
fig.set_ylabel('206084_at')


# plot histogram to check distribution


plt.figure(figsize=(24,20))


plt.subplot(4, 2, 1)
fig = df['241672_at'].hist(bins=20)
fig.set_xlabel('241672_at')
fig.set_ylabel('number of samples')


plt.subplot(4, 2, 2)
fig = df['237509_at'].hist(bins=20)
fig.set_xlabel('237509_at')
fig.set_ylabel('number of samples')


plt.subplot(4, 2, 3)
fig = df['220030_at'].hist(bins=20)
fig.set_xlabel('220030_at')
fig.set_ylabel('number of samples')


plt.subplot(4, 2, 4)
fig = df['230765_at'].hist(bins=20)
fig.set_xlabel('230765_at')
fig.set_ylabel('number of samples')


plt.subplot(4, 2, 5)
fig = df['1556366_s_at'].hist(bins=20)
fig.set_xlabel('1556366_s_at')
fig.set_ylabel('number of samples')


plt.subplot(4, 2, 6)
fig = df['215531_s_at'].hist(bins=20)
fig.set_xlabel('215531_s_at')
fig.set_ylabel('number of samples')


plt.subplot(4, 2, 7)
fig = df['240512_x_at'].hist(bins=20)
fig.set_xlabel('240512_x_at')
fig.set_ylabel('number of samples')


plt.subplot(4, 2, 8)
fig = df['206084_at'].hist(bins=20)
fig.set_xlabel('206084_at')
fig.set_ylabel('number of samples')


X = df.drop(['disease:ch1', 'index'], axis=1)
y = df['disease:ch1']


# split X and y into training and testing sets


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)


# check the shape of X_train and X_test


X_train.shape, X_test.shape
cols = X_train.columns


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train = pd.DataFrame(X_train, columns=[cols])
X_train.describe()
X_test = pd.DataFrame(X_test, columns=[cols])


# import SVC classifier
from sklearn.svm import SVC


# import metrics to compute accuracy
from sklearn.metrics import accuracy_score


# instantiate classifier with default hyperparameters
svc=SVC()


# fit classifier to training set
svc.fit(X_train,y_train)


# make predictions on test set
y_pred=svc.predict(X_test)


# compute and print accuracy score
print('Model accuracy score with default hyperparameters: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


# instantiate classifier with rbf kernel and C=100
svc=SVC(C=100.0)


# fit classifier to training set
svc.fit(X_train,y_train)


# make predictions on test set
y_pred=svc.predict(X_test)


# compute and print accuracy score
print('Model accuracy score with rbf kernel and C=100.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


# instantiate classifier with rbf kernel and C=1000
svc=SVC(C=1000.0)


# fit classifier to training set
svc.fit(X_train,y_train)


# make predictions on test set
y_pred=svc.predict(X_test)


# compute and print accuracy score
print('Model accuracy score with rbf kernel and C=1000.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


# instantiate classifier with linear kernel and C=1.0
linear_svc=SVC(kernel='linear', C=1.0)


# fit classifier to training set
linear_svc.fit(X_train,y_train)


# make predictions on test set
y_pred_test=linear_svc.predict(X_test)


# compute and print accuracy score
print('Model accuracy score with linear kernel and C=1.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred_test)))


# instantiate classifier with linear kernel and C=100.0
linear_svc100=SVC(kernel='linear', C=100.0)


# fit classifier to training set
linear_svc100.fit(X_train, y_train)


# make predictions on test set
y_pred=linear_svc100.predict(X_test)


# compute and print accuracy score
print('Model accuracy score with linear kernel and C=100.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


# instantiate classifier with linear kernel and C=1000.0
linear_svc1000=SVC(kernel='linear', C=1000.0)


# fit classifier to training set
linear_svc1000.fit(X_train, y_train)


# make predictions on test set
y_pred=linear_svc1000.predict(X_test)


# compute and print accuracy score
print('Model accuracy score with linear kernel and C=1000.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


y_pred_train = linear_svc.predict(X_train)


print('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train)))


# print the scores on training and test set
print('Training set score: {:.4f}'.format(linear_svc.score(X_train, y_train)))
print('Test set score: {:.4f}'.format(linear_svc.score(X_test, y_test)))


# check class distribution in test set


y_test.value_counts()


# check null accuracy score


null_accuracy = (31/(31+5))
print('Null accuracy score: {0:0.4f}'. format(null_accuracy))


# instantiate classifier with polynomial kernel and C=1.0
poly_svc=SVC(kernel='poly', C=1.0)


# fit classifier to training set
poly_svc.fit(X_train,y_train)


# make predictions on test set
y_pred=poly_svc.predict(X_test)


# compute and print accuracy score
print('Model accuracy score with polynomial kernel and C=1.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


# instantiate classifier with polynomial kernel and C=100.0
poly_svc100=SVC(kernel='poly', C=100.0)


# fit classifier to training set
poly_svc100.fit(X_train, y_train)


# make predictions on test set
y_pred=poly_svc100.predict(X_test)


# compute and print accuracy score
print('Model accuracy score with polynomial kernel and C=1.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


# instantiate classifier with sigmoid kernel and C=1.0
sigmoid_svc=SVC(kernel='sigmoid', C=1.0)


# fit classifier to training set
sigmoid_svc.fit(X_train,y_train)


# make predictions on test set
y_pred=sigmoid_svc.predict(X_test)


# compute and print accuracy score
print('Model accuracy score with sigmoid kernel and C=1.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


# instantiate classifier with sigmoid kernel and C=100.0
sigmoid_svc100=SVC(kernel='sigmoid', C=100.0)


# fit classifier to training set
sigmoid_svc100.fit(X_train,y_train)


# make predictions on test set
y_pred=sigmoid_svc100.predict(X_test)


# compute and print accuracy score
print('Model accuracy score with sigmoid kernel and C=100.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


# Print the Confusion Matrix and slice it into four pieces


from sklearn.metrics import confusion_matrix


cm = confusion_matrix(y_test, y_pred_test)
print('Confusion matrix\n\n', cm)
print('\nTrue Positives(TP) = ', cm[0,0])
print('\nTrue Negatives(TN) = ', cm[1,1])
print('\nFalse Positives(FP) = ', cm[0,1])
print('\nFalse Negatives(FN) = ', cm[1,0])


# visualize confusion matrix with seaborn heatmap


cm_matrix = pd.DataFrame(data=cm, columns=['Actual Positive:1', 'Actual Negative:0'], index=['Predict Positive:1', 'Predict Negative:0'])


sns.heatmap(cm_matrix, annot=True, fmt='d', cmap='YlGnBu')


from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred_test))
TP = cm[0,0]
TN = cm[1,1]
FP = cm[0,1]
FN = cm[1,0]


# print classification accuracy
classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)
print('Classification accuracy : {0:0.4f}'.format(classification_accuracy))


# print classification error
classification_error = (FP + FN) / float(TP + TN + FP + FN)
print('Classification error : {0:0.4f}'.format(classification_error))


# print precision score
precision = TP / float(TP + FP)
print('Precision : {0:0.4f}'.format(precision))
recall = TP / float(TP + FN)
print('Recall or Sensitivity : {0:0.4f}'.format(recall))
true_positive_rate = TP / float(TP + FN)
print('True Positive Rate : {0:0.4f}'.format(true_positive_rate))
false_positive_rate = FP / float(FP + TN)
print('False Positive Rate : {0:0.4f}'.format(false_positive_rate))
specificity = TN / (TN + FP)
print('Specificity : {0:0.4f}'.format(specificity))


# plot ROC Curve
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_test)
plt.figure(figsize=(6,4))
plt.plot(fpr, tpr, linewidth=2)
plt.plot([0,1], [0,1], 'k--' )
plt.rcParams['font.size'] = 12
plt.title('ROC curve for astrocytoma classifier')
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')
plt.show()


# compute ROC AUC


from sklearn.metrics import roc_auc_score
ROC_AUC = roc_auc_score(y_test, y_pred_test)
print('ROC AUC : {:.4f}'.format(ROC_AUC))


# calculate cross-validated ROC AUC


from sklearn.model_selection import cross_val_score
Cross_validated_ROC_AUC = cross_val_score(linear_svc, X_train, y_train, cv=10, scoring='roc_auc').mean()


print('Cross validated ROC AUC : {:.4f}'.format(Cross_validated_ROC_AUC))
from sklearn.model_selection import KFold


kfold=KFold(n_splits=5, shuffle=True, random_state=0)
linear_svc=SVC(kernel='linear')
linear_scores = cross_val_score(linear_svc, X, y, cv=kfold)


# print cross-validation scores with linear kernel
print('Stratified cross-validation scores with linear kernel:\n\n{}'.format(linear_scores))


# print average cross-validation score with linear kernel
print('Average stratified cross-validation score with linear kernel:{:.4f}'.format(linear_scores.mean()))


rbf_svc=SVC(kernel='rbf')
rbf_scores = cross_val_score(rbf_svc, X, y, cv=kfold)


# print cross-validation scores with rbf kernel
print('Stratified Cross-validation scores with rbf kernel:\n\n{}'.format(rbf_scores))


# print average cross-validation score with rbf kernel
print('Average stratified cross-validation score with rbf kernel:{:.4f}'.format(rbf_scores.mean()))