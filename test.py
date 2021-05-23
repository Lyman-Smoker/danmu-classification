from data import *
from sklearn.externals import joblib
import jieba
import jieba.analyse
import re

def fit_directly(test_string):
    file=open('D:/My Python space/课设1/bad_words_train.txt',mode="r",encoding="utf-8")
    fenci_text=jieba.lcut(test_string)
    trainlines=file.read().splitlines()
    for line in trainlines:
        if re.match(line,test_string):
            if re.match(line,test_string).span() != (0,0):
                return True
    return False

def test(test_string):
    if fit_directly(test_string):
        return True
    nb = joblib.load("train_model.m")
    #读取模型
    testingList=[]
    testingList.append(test_string)
    testlines = jieba_cut1(testingList)  # 测试样本向量化
    resultVec = []  # 测试结果向量集
    for testline in testlines:
        if nb.classify_danmu(testline) == 1:
            return True
    return False
if __name__ == "__main__":
    print(fit_directly('交两个!'))
    print(test('交两个!'))
