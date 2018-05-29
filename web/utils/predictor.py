import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, Imputer
from sklearn.model_selection import train_test_split,cross_val_score


from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


def do(data):
    data = pd.read_csv(data)

    y = data['Target']
    X = data.drop('Target',axis = 1)

    clf_list = [MLPClassifier(),SVC(), KNeighborsClassifier(3), GaussianProcessClassifier(),
                DecisionTreeClassifier(), RandomForestClassifier(),AdaBoostClassifier(),
                GaussianNB(),QuadraticDiscriminantAnalysis()]
    clf_names = ['Neural', 'SVC', 'KNeighbors','Gaussian Process',
                 'Decision Tree', 'Random Forest','AdaBoost','Gaussian NB',
                 'Quadratic Discriminant Analysis']
    score_list = []


    imputer = Imputer()
    scaler = StandardScaler()

    X_np = imputer.fit_transform(X.values)
    X = pd.DataFrame(X_np,columns=X.columns)

    X_s = scaler.fit_transform(X.values)
    X = pd.DataFrame(X_s,columns=X.columns)


    data_np = imputer.fit_transform(data.values)
    data = pd.DataFrame(data_np,columns=data.columns)

    data_s = scaler.fit_transform(data.values)
    data = pd.DataFrame(data_s,columns=data.columns)

    corr = data.corr()
    corr = corr.round(2)
    corr_list = corr.values.tolist()
    corr_columns = corr.columns.tolist()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33)


    for name,clf in zip(clf_names,clf_list):

        scores = cross_val_score(clf,X,y,cv=5)
        score=scores.mean()
        score_list.append([name,score])
        score_list.sort(key = lambda x:x[1],reverse = True)
        for items in score_list:
            items[1] = float("%.2f" % items[1])
    return score_list,corr_list,corr_columns

if __name__ == '__main__':
    print('Invalid Call')
