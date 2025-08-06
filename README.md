# Django项目

这是一个Django Web应用程序项目。

## 项目结构

```
testJango/
├── manage.py          # Django管理脚本
├── oneProject/        # 项目配置目录
│   ├── __init__.py
│   ├── settings.py    # 项目设置
│   ├── urls.py        # URL配置
│   ├── asgi.py        # ASGI配置
│   └── wsgi.py        # WSGI配置
├── .gitignore         # Git忽略文件
└── README.md          # 项目说明
```

## 安装和运行

1. 安装依赖：
```bash
pip install django
```

2. 运行开发服务器：
```bash
python manage.py runserver
```

3. 访问应用：
打开浏览器访问 http://127.0.0.1:8000/

## 开发说明

- 这是一个基础的Django项目框架
- 可以根据需要添加应用、模型、视图等
- 数据库使用SQLite（开发环境）

## 版本控制

使用Git进行版本控制，每次修改后请提交代码：

```bash
git add .
git commit -m "提交说明"
git push origin main
``` 