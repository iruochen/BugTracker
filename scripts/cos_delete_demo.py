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

secret_id = ''  # 替换为用户的 secretId
secret_key = ''  # 替换为用户的 secretKey
region = ''  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

# client.delete_object(
#     Bucket='ruochen-1301954372',
#     Key='p1.jpg',
# )

key_list = [{'Key': 'p1.jpg'}, {'Key': 'wx.png'}]
objects = {
    "Quiet": "true",
    "Object": key_list
}
client.delete_objects(
    Bucket='ruochen-1301954372',
    Delete=objects
)

