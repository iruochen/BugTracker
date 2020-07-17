# wiki-02

## 概要

- wiki删除
- wiki编辑
- markdown编辑器
  - 添加、编辑
  - 预览页面
- markdown 上传图片

## 详细

### 1. wiki删除

### 2. wiki编辑

### 3. markdown编辑器

#### 3.1 编辑 & 预览

- 富文本编辑器，ckeditor
- markdown编辑器，mdeditor

项目中应用markdown编辑器：

- 添加和编辑的页面 textarea 输入框 -> 转换为markdown编辑器

  ```
  1. textarea框通过div包裹以便以后查找并转化为编辑器
  	<div id="editor">...</div>
  	
  2. 应用js和css
      <link rel="stylesheet" href="{% static 'plugin/editor-md/css/editormd.min.css' %}">
      <script src="{% static 'plugin/editor-md/editormd.min.js' %}"></script>
      
  3. 进行初始化
      $(function () {
      	initEditorMd();
      })
      /*
      初始化markdown编辑器（textarea转换为编辑器）
      */
      function initEditorMd() {
          editormd('editor', {
              placeholder: "请输入内容",
              height: 500,
              path: "{% static 'plugin/editor-md/lib/' %}"
          })
      }
      
  4. 全屏
      .editormd-fullscreen {
          z-index: 1001;
      }
  ```

- 预览页面按照markdown格式显示

  ```
  1. 内容区域
      <div id="previewMarkdown">
          <textarea>{{ wiki_object.content }}</textarea>
      </div>
      
  2. 引入css、js
      <link rel="stylesheet" href="{% static 'plugin/editor-md/css/editormd.preview.min.css' %}">
      
      <script src="{% static 'plugin/editor-md/editormd.min.js' %}"></script>
      <script src="{% static 'plugin/editor-md/lib/marked.min.js' %}"></script>
      <script src="{% static 'plugin/editor-md/lib/prettify.min.js' %}"></script>
      <script src="{% static 'plugin/editor-md/lib/raphael.min.js' %}"></script>
      <script src="{% static 'plugin/editor-md/lib/underscore.min.js' %}"></script>
      <script src="{% static 'plugin/editor-md/lib/sequence-diagram.min.js' %}"></script>
      <script src="{% static 'plugin/editor-md/lib/flowchart.min.js' %}"></script>
      <script src="{% static 'plugin/editor-md/lib/jquery.flowchart.min.js' %}"></script>
      
  3. 初始化
      $(function () {
          initPreviewMarkdown();
      });
  
      function initPreviewMarkdown() {
          editormd.markdownToHTML("previewMarkdown", {
              htmlDecode: "style, script, iframe"
          });
      }
  ```



#### 3.2 markdown组件上传本地图片

### 4. 腾讯对象存储

#### 4.1 开通服务

- [腾讯COS](https://cloud.tencent.com/product/cos)

- 开通后会赠送免费额度

#### 4.2 后台

![image-20200717113246619](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717113246619.png)

#### 4.3 创建桶

![image-20200717113355038](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717113355038.png)

#### 4.4 上传文件及查看

- 上传文件

![image-20200717113538778](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717113538778.png)

- 上传后，点击详情，进入后会看到一个对象地址，复制在浏览器打开即可查看文件

![image-20200717113612299](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717113612299.png)

![image-20200717113645144](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717113645144.png)

> “桶” 的概念可以理解为一块区域，或者是一个文件夹，能够进行存取数据

#### 4.5 python实现上传文件

点击概览，我们可以看到SDK文档，打开查找python SDK文档

![image-20200717114047968](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717114047968.png)

```
pip install -U cos-python-sdk-v5
```

```python
# -*- coding=utf-8
# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 BucketName-APPID 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys

secret_id = 'COS_SECRETID'      # 替换为用户的 secretId
secret_key = 'COS_SECRETKEY'      # 替换为用户的 secretKey
region = 'ap-nanjing'     # 替换为用户的 Region

token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
client = CosS3Client(config)
```

> <font color="red">secret_id & secret_key</font>
>
> ![image-20200717120607300](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717120607300.png)
>
> ![image-20200717120708868](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717120708868.png)
>
> ![image-20200717120726633](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717120726633.png)
>
> 
>
> <font color="red">region: 区域</font>
>
> ![image-20200717114514328](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717114514328.png)

```python
# 创建桶
response = client.create_bucket(
    # 桶的名称
    Bucket='ruochen-1301954372'
)
```

> ![image-20200717114922865](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717114922865.png)


```python
# 上传文件
response = client.upload_file(
    Bucket='ruochen-1301954372',
    LocalFilePath='local.txt',  # 本地文件的路径
    Key='picture.jpg',  # 上传到桶之后的文件名
    PartSize=1,  # 上传分成几部分
    MAXThread=10,  # 支持最多的线程数
    EnableMD5=False  # 是否支持MD5
)
print(response['ETag'])
```

###### 4.5.1 上传文件示例代码

```python
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

secret_id = '自己id'  # 替换为用户的 secretId
secret_key = '自己key'  # 替换为用户的 secretKey
region = 'ap-nanjing'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

response = client.upload_file(
    Bucket='ruochen-1301954372',
    LocalFilePath='code.png',  # 本地文件的路径
    Key='p1.jpg',  # 上传到桶之后的文件名
)
print(response['ETag'])
```

![image-20200717124206897](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717124206897.png)

###### 4.5.2 创建桶示例代码

```python
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

secret_id = '自己id'  # 替换为用户的 secretId
secret_key = '自己key'  # 替换为用户的 secretKey
region = 'ap-nanjing'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

response = client.create_bucket(
    Bucket='test-1301954372',
    ACL='public-read',  # private / public-read / public-read-wirte
)
```

![image-20200717124221575](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200717124221575.png)

### 5. 项目中集成cos

- 项目中用到的图片可以放在cos中，防止自己的服务器处理图片时压力过大

#### 5.1 创建项目时创建桶

```python
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

```

```python
bucket = "{}-{}-{}-1301954372".format(name, request.tracer.user.mobile_phone, str(int(time.time())))
region = 'ap-nanjing'
create_bucket(bucket, region)
```

#### 5.1 markdown上传图片到cos

- cos上传文件：接收markdown上传的文件再进行上传到cos
- markdown上传图片