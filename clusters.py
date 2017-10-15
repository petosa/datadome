from numpy import genfromtxt
import numpy
from sklearn.cluster import KMeans
from sklearn import tree
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import confusion_matrix

class Clusters:
    unsupervised = None
    supervised = None
    guess = None
    def __init__(self):
        pass
    def ingest(self):
        self.unsupervised = genfromtxt('unsupervised.csv', delimiter=',')
        self.supervised = genfromtxt('supervised.csv', delimiter=',')
        self.keys = genfromtxt('supervised.csv', delimiter=',', dtype="str")[1:,0]
        # 86% accuracy
        # 32% true positive
        # 93% true negative
        clean = self.supervised[1:,1:]
        all_x = clean[:,0:-1]
        all_y = clean[:,-1].reshape((-1,1))
        train_x = all_x[0:10000,:]
        train_y = all_y[0:10000,:]
        test_x = all_x[10000:,:]
        test_y = all_y[10000:,:]
        clf = BaggingRegressor(n_estimators=100)
        clf = clf.fit(train_x, train_y)
        self.guess = clf.predict(all_x)

    def cluster(self, k):
        clean = self.unsupervised[1:,1:]
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(clean)
        clustered = kmeans.predict(clean)
        return clustered
