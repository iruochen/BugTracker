# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> cos
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/7/17 12:56
@Desc   ：
=================================================='''
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from django.conf import settings


def create_bucket(bucket, region="ap-nanjing"):
    """
    创建桶
    :param bucket: 桶名称
    :param region: 区域
    :return:
    """

    config = CosConfig(Region=region, SecretId=settings.TENCENT_COS_ID, SecretKey=settings.TENCENT_COS_KEY)
    client = CosS3Client(config)

    response = client.create_bucket(
        Bucket=bucket,
        ACL='public-read',  # private / public-read / public-read-wirte
    )

def upload_file(bucket, region, file_object, key):

    config = CosConfig(Region=region, SecretId=settings.TENCENT_COS_ID, SecretKey=settings.TENCENT_COS_KEY)
    client = CosS3Client(config)

    response = client.upload_file_from_buffer(
        Bucket=bucket,
        Body=file_object,  # 文件对象
        Key=key,  # 上传到桶之后的文件名
    )
    # https://ruochen-1301954372.cos.ap-nanjing.myqcloud.com/p1.jpg
    return "https://{}.cos.{}.myqcloud.com/{}".format(bucket, region, key)
