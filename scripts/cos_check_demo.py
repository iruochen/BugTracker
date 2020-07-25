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

secret_id = 'AKIDvbYGiz7AC8qcAw5qZ5UNDE1sSbU6uZry'  # 替换为用户的 secretId
secret_key = 'MQzJ7eeuyATCpLabqqiekBRRcgVkrxoK'  # 替换为用户的 secretKey
region = 'ap-nanjing'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

response = client.head_object(
    Bucket='test-1301954372',
    Key='头1像.jpg'
)
print(response)
