# 重启Python语言服务器

如果自动补全不工作，请按以下步骤操作：

## 方法1: 使用命令面板
1. 按 `Cmd+Shift+P` 打开命令面板
2. 输入 "Python: Restart Language Server"
3. 选择并执行

## 方法2: 重启VS Code
1. 完全关闭VS Code
2. 重新打开VS Code
3. 打开项目文件夹

## 方法3: 检查扩展
1. 按 `Cmd+Shift+X` 打开扩展面板
2. 搜索 "Python"
3. 确保安装了 "Python" 扩展
4. 如果已安装，尝试禁用后重新启用

## 测试自动补全
在 `projects/views.py` 中尝试：
1. 输入 `Http` - 应该提示 `HttpResponse`
2. 输入 `View` - 应该提示 `View`
3. 输入 `def ` - 应该提示函数定义
4. 输入 `self.` - 应该提示方法

## 快捷键
- `Ctrl+Space` - 手动触发建议
- `Ctrl+.` - 快速修复
- `Tab` - 接受建议 