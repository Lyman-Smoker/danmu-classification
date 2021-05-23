import b站弹幕爬取
import train
import bayes
from data import *
from sklearn.externals import joblib
import time

def showAll(rid):
    url = b站弹幕爬取.post_info_data(rid)
    danmu_old=b站弹幕爬取.post_data_url(url)


