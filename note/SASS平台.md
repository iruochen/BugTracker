# SAAS平台
>bug&任务追踪管理

# 涉及知识点
- 虚拟环境，电脑上创建多个python环境
- local_settings.py 本地配置
	
	```
	开发：
		连接数据库需要在django中的setting中设置，连接数据库IP: 1.1.1.1
	测试：
		连接数据库需要在django中的setting中设置，连接数据库IP: 1.1.1.2
	```
	```python
	# settings.py
	try:
		from .local_settings import *
	
	except ImportError:
		pass
	```

	```
	# local_settings.py 中重写配置
	```
	除了local_settings.py 其他给测试, 测试可以自己写一个local_settings.py

- 腾讯云平台（免费额度）
	- sms短信，申请服务。
	- cos对象存储，腾讯给了你云硬盘，项目中上传文件/查看文件/下载文件。

	```
	如果放在自己电脑：
	慢，
	```

- redis

	```
	MySQL: 
		自己的电脑          另外一个电脑
		pymysql模块   ->      MySQL软件 -> 行为:   (硬盘文件操作)
												create table 创建表(创建文件)
												insert table 插入表(写一条记录)

	redis	 
		自己的电脑          另外一个电脑
		redis模块     ->      Redis软件 -> 行为:   (内存操作)
												set name="" 10s，在内存中 name=""
												get name，在内存中获取name对应的值  
	                                            超时时间

	# 注意：1 台电脑可以操作(本地测试)
	```

# 项目开发
- 一期： 用户认证（短信验证、图片验证码、django ModelForm组件）- 3天
- 二期： wiki、文件、问题管理 - 5 ~ 7天
- 三期： 支付、部署 - 2天