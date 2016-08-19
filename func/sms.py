#-*- coding: utf-8 -*-

import json
import requests

__author__  = 'patrick_psq'

# 请求的头部内容
headers = {
  "X-LC-Id": "EY1MSmWwTQiv6qGiz5TqTo2w-gzGzoHsz",
  "X-LC-Key": "jH8Ep9jsV0e83h0rdGUqjwpT",
  "Content-Type": "application/json"
}

# 请求发送验证码
REQUEST_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/requestSmsCode'

# 请求校验验证码
VERIFY_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/verifySmsCode/'


def send_message(phone):
    """
    通过post请求RequestSMSCode API发送验证码到指定手机
    :param phone: 通过网页表单获取的电话号码
    :return:
    """
    data = {'mobilePhoneNumber': phone}

    # POST 方法包含三个参数：
    # REQUEST_SMS_CODE_URL： 请求的URL
    # data：请求的内容，json格式
    # headers：请求的头部
    r = requests.post(REQUEST_SMS_CODE_URL, data=json.dumps(data), headers=headers)

    if r.status_code == 200:  # 请求成功
        return True
    else:
        return False


def verify(phone, code):
    """
    发送post请求到VerifySMSCode API获取校验结果
    :param phone: 通过网页表单获取的电话号码
    :param code: 通过网页表单获取的验证码
    :return:
    """

    # 完整的Verify URL
    target_url = VERIFY_SMS_CODE_URL + '{code}?mobilePhoneNumber={phone}'.format(code=code, phone=phone)

    r = requests.post(target_url, headers=headers)

    if r.status_code == 200:
        return True
    else:
        return False
