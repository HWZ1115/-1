import requests
import random
import time
import os
def signin(token):
    url = 'https://userapi.qiekj.com/signin/signInAcList'
    headers = {
        "Host": "userapi.qiekj.com",
        "Version": "1.50.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    data = {
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    id = response_data['data']['id']
    return id
def sign(id, token):
    url = 'https://userapi.qiekj.com/signin/doUserSignIn'
    headers = {
        "Host": "userapi.qiekj.com",
        "Version": "1.50.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    data = {
        'activityId': id,
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    msg = response_data['msg']
    print(f"当前签到结果:{msg}")
def appgg(token):#APP广告
    url = 'https://userapi.qiekj.com/task/completed'
    headers = {
        "Host": "userapi.qiekj.com",
        "Version": "1.50.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    data = {
        'taskCode':'18893134-715b-4307-af1c-b5737c70f58d',
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    msg = response_data['msg']
    print(f"广告观看结果:{msg}")
def appsp(token):#APP视频
    url = 'https://userapi.qiekj.com/task/completed'
    headers = {
        "Host": "userapi.qiekj.com",
        "Version": "1.50.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    data = {
        'taskCode': 2,
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    msg = response_data['msg']
    print(f"视频观看结果:{msg}")
def appll(token):#APP浏览
    url = 'https://userapi.qiekj.com/task/completed'
    headers = {
        "Host": "userapi.qiekj.com",
        "Version": "1.50.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    data = {
        'taskCode':'22982c2e-f45e-4bd8-b09d-466d9b79144b',
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    msg = response_data['msg']
    print(f"产品浏览结果:{msg}")
def zfbsp(token):#支付宝视频
    url = 'https://userapi.qiekj.com/task/completed'
    headers = {
        "Host": "userapi.qiekj.com",
        "Version": "1.50.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    data = {
        'taskCode': 9,
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    msg = response_data['msg']
    print(f"观看结果:{msg}")
if __name__ == "__main__":
    token = os.environ.get('pgsh')
    if not token:
        print("请设置pgsh环境变量在运行")
    else:
        cks_list = token.split('@')
        num = len(cks_list)
        for num, ck in enumerate(cks_list, start=1):
            print(f"=====开始执行第{num}个用户的任务=====")
            id = signin(ck)
            sign(id, ck)
            for _ in range(8):
                appgg(ck)  # APP广告
                time.sleep(random.randint(15, 25))
            for _ in range(10):
                appsp(ck)  # APP视频
                time.sleep(random.randint(15, 25))
            appll(ck)  # APP浏览
            print("=====开始执行支付宝任务=====")
            for _ in range(10):
                zfbsp(ck)
                time.sleep(random.randint(15, 25))
