# SMSVerification

This is an SMS Verification application implemented by Python.

### Directory Structure

![icon](http://obw22u9v2.bkt.clouddn.com/dir_stru.png)

* func/: 放置自定义模块
  * __init__.py: 空文件，使得该目录可被作为模块导入
  * sms.py: 实现获取短信验证码以及校验验证码的功能
* login.py: 基于Flask的后台，能相应POST与GET请求
* templates/: 存放网页渲染模板
  * login.html: 登陆验证界面
  * success.html: 验证成功界面


### Reference

[实验楼](https://www.shiyanlou.com/courses/609)
