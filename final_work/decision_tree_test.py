from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split
from final_work.decision_tree import classifier
import numpy as np
import time

# 加载数据 鸢尾花数据集（150，4）
iris = datasets.load_iris()
iris_feature = iris.data
iris_target = iris.target

# 划分数据
feature_train, feature_test, target_train, target_test = train_test_split(iris_feature, iris_target, test_size=0.33,
                                                                          random_state=42)
# 创建决策树及验证准确率
time_start = time.time()
clf = classifier()
clf.train(feature_train, target_train)
clf.predict(feature_test)
score = clf.accuracy(target_test)
time_end = time.time()
print('score of iris is ' + str(score))
print('time is' + str(time_end - time_start))

# 加载数据，葡萄酒数据集（178，13）
wine = datasets.load_wine()
wine_feature = wine.data
wine_target = wine.target

# 划分数据
feature_train, feature_test, target_train, target_test = train_test_split(wine_feature, wine_target, test_size=0.33,
                                                                          random_state=42)
# 创建决策树及验证准确率
time_start = time.time()
clf = classifier()
clf.train(feature_train, target_train)
clf.predict(feature_test)
score = clf.accuracy(target_test)
time_end = time.time()
print('score of wine is ' + str(score))
print('time is' + str(time_end - time_start))

# # 加载数据 cancer数据集(569, 30)
# cancer = datasets.load_breast_cancer()
# cancer_feature = cancer.data
# cancer_target = cancer.target
#
# # 划分数据
# feature_train, feature_test, target_train, target_test = train_test_split(cancer_feature, cancer_target, test_size=0.33,
#                                                                           random_state=42)
# # 创建决策树及验证准确率
# time_start = time.time()
# clf = classifier()
# clf.train(feature_train, target_train)
# clf.predict(feature_test)
# score = clf.accuracy(target_test)
# time_end = time.time()
# print('score of cancer is ' + str(score))
# print('time is' + str(time_end - time_start))

# time_start = time.time()
# clf = tree.DecisionTreeClassifier()
# clf.fit(feature_train, target_train)
# clf.predict(feature_test)
# score = clf.score(feature_test, target_test, sample_weight=None)
# time_end = time.time()
# print("Accuracy of sklearn-DecisionTree: %f" % score)
# print("Runtime of sklearn-DecisionTree:", time_end-time_start)
