# VS Code Python 智能提示配置

## 已完成的配置

### 1. 安装的包
- `django-stubs`: Django类型提示支持（仅用于智能提示，不进行严格检查）

### 2. 配置文件
- `.vscode/settings.json`: VS Code Python设置（已关闭严格类型检查）
- `pyrightconfig.json`: Python类型检查配置（已关闭严格类型检查）

## 使用智能导入提示的方法

### 方法1: 自动导入
1. 输入类名（如 `View`）
2. 按 `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)
3. 选择 "Python: Add Import"
4. 选择正确的导入路径

### 方法2: 快速修复
1. 将光标放在未导入的类名上
2. 按 `Ctrl+.` (Mac: `Cmd+.`)
3. 选择 "Add import for 'View'"

### 方法3: 自动完成
1. 输入类名时，VS Code会显示导入建议
2. 选择建议会自动添加导入语句

## 常用Django导入

```python
# Views
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# HTTP
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

# Models
from django.db import models
from django.contrib.auth.models import User

# Forms
from django import forms
from django.forms import ModelForm

# URLs
from django.urls import path, include, reverse, reverse_lazy

# Authentication
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
```

## 故障排除

如果智能提示不工作：
1. 重启VS Code
2. 按 `Ctrl+Shift+P` 选择 "Python: Restart Language Server"
3. 确保Python解释器路径正确
4. 检查是否安装了Python扩展

## 快捷键
- `Ctrl+Space`: 触发建议
- `Ctrl+.`: 快速修复
- `Ctrl+Shift+P`: 命令面板
- `F12`: 转到定义
- `Shift+F12`: 查找所有引用 