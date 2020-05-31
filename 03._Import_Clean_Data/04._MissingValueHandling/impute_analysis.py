# %%

# Import library for file handling
import os

# %%

# Import library for data processing
import pandas as pd
import statsmodels.api as sm
from sklearn.impute import SimpleImputer
from fancyimpute import KNN
from fancyimpute import IterativeImputer
#%%

# Import library for plotting
from matplotlib import pyplot as plt

# %%

# Import diabetes file as pandas DataFrame
diabetes = pd.read_csv(os.path.join('00._data', 'pima-indians-diabetes-data.csv'))

#%%

# Display head
print(diabetes.head())
print(diabetes.info())

#%%

diabetes_cc = diabetes.dropna(how='any')
X = sm.add_constant(diabetes_cc.iloc[:, :-1])
y = diabetes_cc['Class']
lm = sm.OLS(y, X).fit()

#%%

print(lm.summary())

#%%

print(lm.rsquared_adj)

#%%

print(lm.params)

#%%

# Create Imputation DataFrame

# Mean Imputation
diabetes_mean_imputed = diabetes.copy(deep=True)
diabetes_mean_imputed.iloc[:, :] = SimpleImputer(strategy='mean').fit_transform(diabetes_mean_imputed)

# KNN Imputation
knn_imputer = KNN()
diabetes_knn_imputed = diabetes.copy(deep=True)
diabetes_knn_imputed.iloc[:, :] = knn_imputer.fit_transform(diabetes_knn_imputed)

# MICE Imputation
mice_imputer = IterativeImputer()
diabetes_mice_imputed = diabetes.copy(deep=True)
diabetes_mice_imputed.iloc[:, :] = mice_imputer.fit_transform(diabetes_mice_imputed)

#%%

# Mean Imputation
X = sm.add_constant(diabetes_mean_imputed.iloc[:, :-1])
y = diabetes['Class']
lm_mean = sm.OLS(y, X).fit()
# KNN Imputation
X = sm.add_constant(diabetes_knn_imputed.iloc[:, :-1])
lm_KNN = sm.OLS(y, X).fit()
# MICE Imputation
X = sm.add_constant(diabetes_mice_imputed.iloc[:, :-1])
lm_MICE = sm.OLS(y, X).fit()

#%%

# Comparing R-squared of different imputations
print(pd.DataFrame({'Complete': lm.rsquared_adj,
                    'Mean Imp.': lm_mean.rsquared_adj,
                    'KNN Imp.': lm_KNN.rsquared_adj,
                    'MICE Imp.': lm_MICE.rsquared_adj},
                   index=['R_squared_adj']))

#%%

# Comparing coefficients of different imputations
print(pd.DataFrame({'Complete': lm.params,
                    'Mean Imp.': lm_mean.params,
                    'KNN Imp.': lm_KNN.params,
                    'MICE Imp.': lm_MICE.params}))

#%%

# Comparing density plots
diabetes_cc['Skin_Fold'].plot(kind='kde', c='red', linewidth=3)
diabetes_mean_imputed['Skin_Fold'].plot(kind='kde')
diabetes_knn_imputed['Skin_Fold'].plot(kind='kde')
diabetes_mice_imputed['Skin_Fold'].plot(kind='kde')
labels = ['Baseline (Complete Case)', 'Mean Imputation', 'KNN Imputation', 'MICE Imputation']
plt.legend(labels)
plt.xlabel('Skin Fold')
plt.show()
