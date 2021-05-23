import bayes
from data import *
from sklearn.externals import joblib
import time
if __name__ == "__main__":
    pos = "D:/My Python space/课设1/good_words_train.txt"
    neg = "D:/My Python space/课设1/bad_words_train.txt"

    #训练模型开始时间
    start = time.process_time()

    print("正在获取训练矩阵及其分类向量")
    trainingList,classVec = loadDataSet(pos,neg)

    print("正在将训练矩阵分词，并生成词表")
    vocabList,trainMat = jieba_cut(trainingList) #创建词汇表

    bayes = bayes.BerNB(vocabList)

    print("正在训练模型")
    bayes.trainNB(trainMat,classVec)


    print("保存模型")
    joblib.dump(bayes, "train_model.m")

    print ("训练模型使用了：" + str(time.process_time() - start) + '秒\n')