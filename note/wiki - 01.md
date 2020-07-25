# wiki

## 概要

- 表结构设计
- 快速开发
- 应用markdown组件
- 腾讯COS做上传

## 详细

### 1. 表结构设计

| ID   | 标题 | 内容 | 项目ID | 父ID | 深度 |
| ---- | ---- | ---- | ------ | ---- | ---- |
| 1    | test | xxxx | x      | null | 1    |
| 2    | xx   | aaaa | x      | null | 1    |
| 3    | xx   | bbbb | x      | 1    | 2    |

```python
class Wiki(models.Model):
    project = models.ForeignKey(verbose_name='项目', to='Project')
    title = models.CharField(verbose_name='标题', max_length=32)
    content = models.TextField(verbose_name='内容')

    # 自关联
    parent = models.ForeignKey(verbose_name='父文章', to='Wiki', null=True, blank=True, related_name='children')
```



### 2. 快速开发

#### 2.1 wiki首页展示

- 首页

  ![image-20200715172634904](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200715172634904.png)

- 多级目录

  ```
  模板渲染：
  	- 数据库中获取的数据要有层级的划分
  		queryset = models.Wiki.object.filter(project_id=2)
  		将数据构造
  		[
  			{
  				id: 1,
  				title: 'ruochen',
  				children: [
  					{
  						id: xxx,
  						name: 'xxx',
  					}
  				]
  			}
  		]
      - 页面展示，循环显示（不知道有多少层）
      	递归
          
      缺点：
      	- 代码实现难
      	- 效率低
  ```

  ```
  后端 + 前端完成ajax+ID选择器
  	- 前端： 打开页面之后，发送ajax请求获取所有的文档标题信息
  	- 后台： 获取所有的文章信息
  		queryset = models.Wiki.object.filter(project_id=2).values_list('id', 'title', 'parent_id')
  		[
  			{'id'； 1， ‘title': 'ruochen', parent_id: None},
  			{'id': 2, 'title': '1111', parent_id: None},
  			{'id': 3, 'title': '2222', parent_id: None},
  			{'id': 4, 'title': '3333', parent_id: 3},
  			{'id': 5, 'title': '4444', parent_id: 1},
  		]
  		直接返回给前端的ajax
  	- ajax的回调函数success中获取到 res.data, 并循环
  		$.each(res.data, function(index, item){
  			if(item.parent_id){
  			
  			}else{
  				
  			}
  		})
  		
  <ul>
  	<li id="1">ruochen
  		<ul>
          	<li id="5">4444</li>
          </ul>
  	</li>
  	<li id="2">1111</li>
  	<li id="3">2222
          <ul>
          	<li id="4">3333</li>
          </ul>
  	</li>
  	
  </ul>
  ```

  

存在两个问题

- 父目录要提前出现（编辑）： 排序 + 字段（深度depth）
- 点击目录查看文章详细

#### 2.2 添加文章

#### 2.3 预览文章

#### 2.4 修改文章

#### 2.5 删除文章