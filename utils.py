import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import cross_validate


def plot_percentage_bar_chart(df1,
                              df2,
                              feature,
                              index=None,
                              figsize=None,
                              rot=45,
                              title=None,
                              xlabel=None,
                              ylabel=None,
                              save=False,
                              path='./imgs',
                              show=False):
    font = {'size': 15}
    plt.rc('font', **font)

    total = df1[feature].value_counts().sort_values()
    problem = df2[feature].value_counts().sort_values()
    frac = np.divide(problem, total)

    if index is not None:
        frac.rename(index=index, inplace=True)

    frac.plot(kind='bar',
              figsize=figsize,
              legend=True,
              rot=rot)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    if save:
        if not os.path.exists(os.path.join(path)):
            os.mkdir(path)
        img_path = os.path.join(path, f'{title}.jpg')
        plt.savefig(img_path, bbox_inches='tight', pad_inches=0.5)
    if show:
        plt.show()


def plot_normalized_bar_chart(df1,
                              df2,
                              feature,
                              nb_bins=8,
                              index=None,
                              figsize=None,
                              rot=45,
                              title=None,
                              xlabel=None,
                              save=False,
                              path='./imgs',
                              show=False):
    font = {'size': 15}
    plt.rc('font', **font)

    try:
        bins = pd.cut(df1[feature], bins=nb_bins, retbins=True)[1]
    except TypeError:
        bins = None

    total = df1[feature].value_counts(bins=bins).sort_index()
    total_frac = np.divide(total, total.sum())

    problem = df2[feature].value_counts(bins=bins).sort_index()
    problem_frac = np.divide(problem, problem.sum())

    frac_df = pd.DataFrame({'Total': total_frac, 'Problem': problem_frac})

    if index is None:
        index = total_frac.index.values
    frac_df.index = index

    frac_df.plot(kind='bar',
                 figsize=figsize,
                 legend=True,
                 rot=rot)
    plt.title(title)
    plt.xlabel(xlabel)

    if save:
        if not os.path.exists(os.path.join(path)):
            os.mkdir(path)
        img_path = os.path.join(path, f'{title}.jpg')
        plt.savefig(img_path, bbox_inches='tight', pad_inches=0.5)
    if show:
        plt.show()


def plot_normalized_histogram(df1,
                              df2,
                              feature,
                              nb_bins=8,
                              vertical_lines=False,
                              figsize=None,
                              title=None,
                              xlabel=None,
                              save=False,
                              path='./imgs',
                              show=False):
    font = {'size': 15}
    plt.rc('font', **font)

    plt.figure(figsize=figsize)
    plt.hist([df1[feature], df2[feature]],
             density=True, bins=nb_bins, label=['Total', 'Problem'])
    plt.legend()
    plt.xlabel(xlabel)
    plt.title(title)

    if vertical_lines:
        plt.axvline(df1[feature].mean(), linewidth=2, color='#1f77b4')
        plt.axvline(df2[feature].mean(), linewidth=2, color='#ff7f0e')

    if save:
        if not os.path.exists(os.path.join(path)):
            os.mkdir(path)
        img_path = os.path.join(path, f'{title}.jpg')
        plt.savefig(img_path, bbox_inches='tight', pad_inches=0.5)
    if show:
        plt.show()


def find_the_elbow(X,
                   figsize=None,
                   title=None,
                   save=False,
                   path='./imgs',
                   show=False):
    font = {'size': 15}
    plt.rc('font', **font)

    info_gain_ratio = {}
    for i in range(1, len(X.columns) + 1):
        pca = PCA(n_components=i)
        sc = StandardScaler()
        X_scaled = sc.fit_transform(X)
        x_scaled_pca = pca.fit_transform(X_scaled)
        info_gain_ratio[i] = sum(pca.explained_variance_ratio_)
    pd.DataFrame.from_dict(info_gain_ratio, orient='index', columns=[
                           'Infomation Gain Ratio']).plot(figsize=figsize)
    plt.xlabel('Number of components')
    plt.ylabel('Ratio')
    plt.title(title)
    if save:
        if not os.path.exists(os.path.join(path)):
            os.mkdir(path)
        img_path = os.path.join(path, f'{title}.jpg')
        plt.savefig(img_path, bbox_inches='tight', pad_inches=0.5)
    if show:
        plt.show()


def regression_model_selection(X, y, estimator):
    model = Pipeline([
        ('scale', StandardScaler()),
        ('estimator', estimator)
    ])
    validation = cross_validate(model, X, y, cv=5, scoring=[
                                'neg_mean_squared_error', 'neg_root_mean_squared_error', 'r2'])
    result = {}
    for score in validation:
        result[score] = f'{round(validation[score].mean(), 5)}+-{round(validation[score].std(), 5)}'
    return result


def build_regression_model(estimator,
                           model_name,
                           X_train,
                           y_train,
                           save=False,
                           path='./models'):
    model = Pipeline([
        ('scale', StandardScaler()),
        ('estimator', estimator)
    ])
    model.fit(X_train, y_train)
    if save:
        if not os.path.exists(os.path.join(path)):
            os.mkdir(path)
        model_path = os.path.join(path, f'{model_name}.pkl')
        with open(model_path, 'wb') as file:
            pickle.dump(model, file)
    return model


def evaluate_regression_model(model,
                              X_test,
                              y_test,
                              figsize=None,
                              title=None,
                              save=False,
                              path='./imgs',
                              show=False):
    font = {'size': 15}
    plt.rc('font', **font)

    y_pred = model.predict(X_test)

    r2 = '\nR2: {:.5f}'.format(r2_score(y_test, y_pred))
    mse = '\nMSE: {:.5f}'.format(mean_squared_error(y_test, y_pred))
    rmse = '\nRMSE: {:.5f}'.format(
        mean_squared_error(y_test, y_pred, squared=False))

    plt.figure(figsize=figsize)
    sns.kdeplot(y_test, color='r', label='Actual Value')
    sns.kdeplot(y_pred, color='b', label='Fitted Value')
    plt.legend()
    plt.xlabel('Minutes\n' + r2 + mse + rmse)
    plt.title(title)
    if save:
        if not os.path.exists(os.path.join(path)):
            os.mkdir(path)
        img_path = os.path.join(path, f'{title}.jpg')
        plt.savefig(img_path, bbox_inches='tight', pad_inches=0.5)
    if show:
        plt.show()


def classifier_model_selection(X, y, estimator):
    y = LabelEncoder().fit_transform(y.values)
    model = Pipeline([
        ('scale', StandardScaler()),
        ('estimator', estimator)
    ])
    validation = cross_validate(model, X, y, cv=5, scoring=[
                                'recall', 'precision', 'accuracy', 'f1'])
    result = {}
    for score in validation:
        result[score] = f'{round(validation[score].mean(), 5)}+-{round(validation[score].std(), 5)}'
    return result


def build_classifier_model(estimator,
                           model_name,
                           X_train,
                           y_train,
                           save=False,
                           path='./models'):
    model = Pipeline([
        ('scale', StandardScaler()),
        ('estimator', estimator)
    ])
    model.fit(X_train, y_train)
    if save:
        if not os.path.exists(os.path.join(path)):
            os.mkdir(path)
        model_path = os.path.join(path, f'{model_name}.pkl')
        with open(model_path, 'wb') as file:
            pickle.dump(model, file)
    return model


def evaluate_classifier_model(model,
                              X_test,
                              y_test,
                              figsize=None,
                              title=None,
                              save=False,
                              path='./imgs',
                              show=False):
    font = {'size': 15}
    plt.rc('font', **font)

    y_pred = model.predict(X_test)

    recall = '\nRecall: {:.5f}'.format(recall_score(y_test, y_pred))
    precision = '\nPrecision: {:.5f}'.format(precision_score(y_test, y_pred))
    accuracy = '\nAccuracy: {:.5f}'.format(accuracy_score(y_test, y_pred))
    f1 = '\nF1: {:.5f}'.format(f1_score(y_test, y_pred))

    plt.figure(figsize=figsize)
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='BrBG',
                cbar=False, annot_kws={'size': 15})
    plt.ylabel('True label')
    plt.xlabel('Predicted label\n' + recall + precision + accuracy + f1)
    plt.title(title)

    if save:
        if not os.path.exists(os.path.join(path)):
            os.mkdir(path)
        img_path = os.path.join(path, f'{title}.jpg')
        plt.savefig(img_path, bbox_inches='tight', pad_inches=0.5)
    if show:
        plt.show()
