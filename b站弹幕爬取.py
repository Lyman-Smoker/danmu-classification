#!/usr/bin/env python    用python执行
#-*- coding:utf-8 -*-    #告诉不同系统和不同版本的python用同一种编码格式
#该代码适用与B站直播的弹幕爬取
import requests

#定义一个需要发送的表单
def post_info_data(rid):
    form_data = {"roomid": rid, "csrf_token": "", "csrf": "", "visit_id": ""}
    return form_data

#发送已经打包好的数据
def post_data_url(data):
    url='https://api.live.bilibili.com/ajax/msg'
    response=requests.post(url,data=data)        #发送数据得到响应
    data=response.json()['data']['room']
    itemcont=[]
    itemnick=[]
    for items in data:
        itemcont.append(items['text'])
        itemnick.append(items['nickname'])
    return itemnick[-1],itemcont[-1]

if __name__ == "__main__":
    i=1
    rid="4350043"
    url=post_info_data(rid)
    nick_old,danmu_old=post_data_url(url)
    # print(str(i)+"、"+nick_old+" : "+danmu_old)
    print(danmu_old)
    while True:

        nick_new,danmu_new=post_data_url(url)
        if not ((danmu_new == danmu_old) or (nick_old == nick_new)):
            i+=1
            # print(str(i)+"、"+nick_new+" : "+danmu_new)
            print(danmu_new)
            danmu_old=danmu_new