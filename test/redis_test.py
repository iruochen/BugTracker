# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> redis_test
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/6/21 21:34
@Desc   ：
=================================================='''
import redis

# 直接连接redis
conn = redis.Redis(host='192.168.1.4', port=6379, password='root', encoding='utf-8')

# 设置键值： 18203503747="6666" 且超时时间为10s（值写入到redis时会自动转字符串）
conn.set('18203503747', 'ruochen', ex=10)

# 根据键获取值： 如果存在获取值（获取到的是字节类型）；不存在则返回 None
value = conn.get('18203503747')
print(value)
print(value.decode())
