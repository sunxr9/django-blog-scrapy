## 个人博客

—— 基于django1.10以及bootstrap3.0

----------
### 简介
> 目前博客功能拥有基本的分页、评论、详细阅读的功能

----------

>今天为博客增添了按标题搜索的功能

----------
>历经千辛万苦，终于将博客部署到好了，点击进入[我的博客][2]

------------

>今天对博客的页面以及代码进行了优化，同时，添加了阅读量随点击增加的功能
```python
class ArticleDetailView(DetailView):
	......
 # 从数据库中获取id为pk_url_kwargs的对象
    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        # 点击一次阅读量增加一次
        obj.views += 1
        obj.save()
        obj.body = markdown.markdown(obj.body, safe_mode='escape',
        extensions=[
            'markdown.extensions.nl2br',
            'markdown.extensions.fenced_code'
        ])
        return obj
	......
```

------------

>今天为我的博客添加了标签云的功能，其实现原理与目录实现原理基本一致,不同点在于，与Article数据库的关系变成了ManyToMany类型

------------

>今天为我的博客添加了网页意见提出功能, 用户通过在'''关于'''界面的意见栏写下意见, 将意见信息保存到数据库并发送意见给我自己并返回感谢界面

------------

>由于markdown2不能解析篱笆型代码块，故将其替换为了markdown

--------

>添加日志配置

--------

>添加[Redis][4]用以缓存文章界面

--------

>添加[Celery][3]异步处理请求(我用来处理发送邮件时, 可能造成的阻塞(ps.没什么访问量，其实并不会发生- -))

--------

>写了一个中间件, 用以在调试的时候, 将每次的数据库操作都打印到命令行上. [代码参考][5]

--------

>用docker重新部署了我的django博客应用，并已写成[教程][6]供大家参考

--------

>由于此博客的线上版本已下线，需要大家自行clone，然后运行，我这里简单介绍clone下来后，安装方面需要注意的问题
- 首先需要安装相关数据库，我这里用mysql做示范(鉴于大家的普遍使用), [ubuntu安装参考][7], 然后创建一个名为blog的数据库
- (可选)redis 安装， [安装参考][8]，然后启动redis
- 新建一个虚拟环境，然后安装相关模块```pip install -r requirements/dev.txt```
- 初始化表```python manage.py migrate```
- 最后运行```python manage.py runserver```

--------

  [2]: http://www.sssinedge.xyz/
  [3]: http://docs.celeryproject.org/en/latest/index.html
  [4]: https://redis.io/
  [5]: https://djangosnippets.org/snippets/264/
  [6]: https://tomming233.github.io/2017/04/24/%E7%94%A8docker%E9%83%A8%E7%BD%B2django%E5%BA%94%E7%94%A8/
  [7]: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04
  [8]: https://redis.io/topics/quickstart
