# 测试自动补全功能
from django.http import HttpResponse
from django.views import View

# 测试输入以下内容时是否有自动补全：
# 1. 输入 "Http" 应该提示 "HttpResponse"
# 2. 输入 "View" 应该提示 "View"
# 3. 输入 "def " 应该提示函数定义
# 4. 输入 "self." 应该提示方法

class TestView(View):
    def get(self, request):
        # 在这里输入 "Http" 应该提示 "HttpResponse"
        return HttpResponse("测试自动补全")
    
    def post(self, request):
        # 在这里输入 "self." 应该提示方法
        return HttpResponse("POST请求") 