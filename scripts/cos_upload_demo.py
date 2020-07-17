# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> cos_upload_demo
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/17 11:52
@Desc   ：
=================================================='''
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'AKIDvbYGiz7AC8qcAw5qZ5UNDE1sSbU6uZry'  # 替换为用户的 secretId
secret_key = 'MQzJ7eeuyATCpLabqqiekBRRcgVkrxoK'  # 替换为用户的 secretKey
region = 'ap-nanjing'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

response = client.upload_file(
    Bucket='ruochen-1301954372',
    LocalFilePath='code.png',  # 本地文件的路径
    Key='p1.jpg',  # 上传到桶之后的文件名
)
print(response['ETag'])
