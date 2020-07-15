# wiki

## 概要

- 表结构设计
- 快速开发
- 应用markdown组件
- 腾讯COS做上传

## 详细

### 1. 表结构设计

| ID   | 标题 | 内容 | 项目ID | 父ID |
| ---- | ---- | ---- | ------ | ---- |
| 1    | test | xxxx | x      | null |
| 2    | xx   | aaaa | x      | null |
| 3    | xx   | bbbb | x      | 1    |

```python
class Wiki(models.Model):
    project = models.ForeignKey(verbose_name='项目', to='Project')
    title = models.CharField(verbose_name='标题', max_length=32)
    content = models.TextField(verbose_name='内容')

    # 自关联
    parent = models.ForeignKey(verbose_name='父文章', to='Wiki', null=True, blank=True, related_name='children')
```

