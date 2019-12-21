import numpy as np
import operator as op
import math
import pickle


# 数据归一化
def normalization(data):
    # 按列取最值，也就是说求每个特征的最值
    min_value = data.min(axis=0)
    max_value = data.max(axis=0)
    # 取差值
    diff = max_value - min_value
    # map归1化
    norm_data = (data - min_value) / diff
    return norm_data


# 决策树节点
class node:
    def __init__(self, index=-1, value=None, results=None, right_tree=None, left_tree=None):
        self.index = index  # 用于记录当前节点选择的特征的下标
        self.value = value  # 记录对应特征的阈值选择
        self.right_tree = right_tree
        self.left_tree = left_tree
        self.results = results  # 记录分类结果，叶节点用到


# 决策树
class classifier:
    def __init__(self):
        self.tree_node = None  # 节点
        self.prediction = None  # 用于记录预测值

    # 训练，包括数据处理和建树
    def train(self, train_data, train_label):
        # 数据处理，归1化
        train_data = normalization(train_data)
        # 将label向量重塑为单列矩阵
        train_label = np.expand_dims(train_label, axis=1)
        # 矩阵拼接
        data = np.hstack([train_data, train_label])
        # 创建决策树
        self.tree_node = self.create_tree(data)

        return self

    # 创建决策树
    # data 包含feature和label
    def create_tree(self, data):
        # 非空判断
        if len(data) == 0:
            self.tree_node = node()
            return self.tree_node

        # 如果只剩唯一的标签了，直接返回叶节点
        if len(np.unique(data[:, -1])) == 1:
            self.tree_node = node(results=self.unique_count(data[:, -1]))
            return self.tree_node

        # 如果只剩下唯一的一列lable数据还没有判断完成，则保存所有的未完成数据
        if data.shape[1] == 1:
            # print('not finished')
            self.tree_node = node(results=self.unique_count(data[:, -1]))
            return self.tree_node

        # 初始化临时数据
        best_gain = 0.0  # 记录最大熵增
        best_criteria = None  # 记录最优的特征选择以及对应的阈值
        best_set = None  # 记录最优的划分形式

        feature_num = data.shape[1] - 1  # 获取特征的维度
        sample_num = data.shape[0]  # 获取训练集的数目
        init_entropy = self.get_entropy(data[:, -1])  # 计算初始熵

        # 遍历所有的特征，计算熵增
        for i in range(feature_num):
            uniques = np.unique(data[:, i])  # 获取所有不同的特征的值
            for value in uniques:
                left_set, right_set = self.divide_data(data, i, value)  # 根据所有互异的数据对数据进行划分，同时删除了用于划分的特征
                ratio = float(len(left_set) / sample_num)  # 计算划分比例
                # 计算熵增
                if ratio <= 0.0:  # 全右
                    info_gain = init_entropy - (1 - ratio) * self.get_entropy(right_set[:, -1])
                elif ratio >= 1.0:  # 全左
                    info_gain = init_entropy - ratio * self.get_entropy(left_set[:, -1])
                else:
                    info_gain = init_entropy - ratio * self.get_entropy(left_set[:, -1]) - (
                            1 - ratio) * self.get_entropy(right_set[:, -1])

                # 保存临时结果
                if info_gain > best_gain:
                    best_gain = info_gain
                    best_criteria = (i, value)
                    best_set = (left_set, right_set)

        # 递归构建决策树
        l_tree = self.create_tree(best_set[0])
        r_tree = self.create_tree(best_set[1])
        self.tree_node = node(index=best_criteria[0], value=best_criteria[1], left_tree=l_tree,
                              right_tree=r_tree)
        return self.tree_node

    # 使用创建好的决策树预测数据
    def predict(self, test_data):
        # 归1化
        test_data = normalization(test_data)
        # 初始化一些临时变量
        test_num = test_data.shape[0]  # 测试集的数量
        prediction = np.zeros([test_num, 1])  # 预测结果初始化为0
        # 获取预测值
        for i in range(test_num):
            result = self.classify(test_data[i, :], self.tree_node)
            result = sorted(result.items(), key=op.itemgetter(1), reverse=True)  # 取得数目最多的分类
            prediction[i] = result[0][0]  # 获取分类

        self.prediction = prediction
        return prediction

    # 计算准确率
    def accuracy(self, test_label):
        test_label = np.expand_dims(test_label, axis=1)
        prediction = self.prediction
        acc = sum(prediction == test_label) / len(test_label)
        return acc

    # 保存决策树
    def save(self, filename):
        f = open(filename, 'w')
        pickle.dump(self.tree_node, f)
        f.close()

    # 加载决策树
    def load(self, filename):
        f = open(filename)
        self.tree_node = pickle.load(f)
        return self

    # 计算熵
    def get_entropy(self, labels):
        labels_num = len(labels)  # label的数目
        label_count = self.unique_count(labels)  # label的种类和数目的字典

        entropy = 0.0
        for j in label_count:
            prop = label_count[j] / labels_num  # 使用最大似然估计模拟概率
            entropy = entropy + (-prop * math.log(prop, 2))

        return entropy

    # 获取label的种类和数目的字典
    def unique_count(self, labels):
        label_count = {}
        for i in range(len(labels)):
            label_count[labels[i]] = label_count.get(labels[i], 0) + 1
        return label_count

    # 划分数据，用于计算熵增，
    # 划分的同时删除了作为划分标准的特征值，也就是得到了补集
    # index 根据哪一列的值划分
    # value 划分的阈值
    def divide_data(self, data, index, value):
        left_set = []  # 小于阈值的集合
        right_set = []  # 大于阈值的集合

        for temp in data:
            if temp[index] >= value:
                new_feature = np.delete(temp, index)  # 删除特征，计算熵增时需要用到补集
                right_set.append(new_feature)  # 添加到集合中
            else:
                new_feature = np.delete(temp, index)
                left_set.append(new_feature)
        return np.array(left_set), np.array(right_set)

    # 获取分类结果
    def classify(self, sample, tree):
        # 如果是叶节点，直接返回
        if tree.results is not None:
            return tree.results

        # 从根节点开始，递归到叶节点
        value = sample[tree.index]  # 根据index获取当前节点的用于判断的特征值
        if value >= tree.value:  # value记录了阈值
            branch = tree.right_tree
        else:
            branch = tree.left_tree
        return self.classify(sample, branch)

    # todo,把树打印出来
    def print_tree(self):
        print('print_tree')

    # todo,树的剪枝
    def cut(self):
        print('cut')
