import b站弹幕爬取
import test

if __name__ == "__main__":
    rid="21144080"
    i=1
    url=b站弹幕爬取.post_info_data(rid)
    nick_old,danmu_old=b站弹幕爬取.post_data_url(url)
    if not test.test(danmu_old):
        # print(test.test(danmu_old))
        print(danmu_old)
    while True:
        nick_new,danmu_new=b站弹幕爬取.post_data_url(url)
        if not ((danmu_new == danmu_old) or (nick_old == nick_new)):
            if not test.test(danmu_new):
                # print(test.test(danmu_new))
                i+=1
                print(danmu_new)
            danmu_old=danmu_new