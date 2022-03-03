# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> cos_check_demo
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/25 10:48
@Desc   ：
=================================================='''

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = ''  # 替换为用户的 secretId
secret_key = ''  # 替换为用户的 secretKey
region = ''  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

response = client.head_object(
    Bucket='test-1301954372',
    Key='头1像.jpg'
)
print(response)
