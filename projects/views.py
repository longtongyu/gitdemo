import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
def index(requests):
    return HttpResponse("zheli yong yingwen")


# def detail(requests,ids):
#     return HttpResponse("这是测试返回的项目1数据",status=100)




class ProjectView(View):

    def get(self, request,pid):
        return HttpResponse(content=f"获取id为{pid}的项目详情数据")

    
    def post(self, request,pid):
        return HttpResponse(content=f"创建id为{pid}的项目详情数据")

    
    def put(self,request,pid):
        return HttpResponse(content=f"更新id为{pid}的项目详情数据")

    
    def delete(self,request,pid):
        return HttpResponse(content=f"删除id为{pid}的项目详情数据")



class MyViewParmForReuqest(View):

    def get(self,request,pid):
        print(f"进入MyViewParmForReuqest.get方法，pid={pid}")  # 调试信息
        name = request.GET.GET("name")
        age = request.GET.get("age")  
        return HttpResponse(content=f"姓名为:{name},年龄为：{age}")

    
    #body参数
    def post(self,request,pid):
        print(f"进入MyViewParmForReuqest.post方法，pid={pid}") 
        if request.content_type == "application/x-www-form-urlencoded":
            return HttpResponse(f"使用application/x-www-form-urlencoded时，姓名：{request.POST.get('name')},年龄：{request.POST.get('age')}") # 调试信息
        elif request.content_type == "multipart/form-data":
            file_data = request.FILES
            # 获取上传的文件
            uploaded_file = request.FILES.get('file')  # 假设前端表单字段名为 'file'
            
            if uploaded_file:
                # 方法1：保存到项目根目录
                with open(f"{uploaded_file.name}", "wb") as file:
                    for chunk in uploaded_file.chunks():
                        file.write(chunk)
                
                return HttpResponse(f"使用multipart/form-data时，姓名：{request.POST.get('name')},年龄：{request.POST.get('age')},文件已保存到：项目根目录")
            else:
                return HttpResponse(f"使用multipart/form-data时，姓名：{request.POST.get('name')},年龄：{request.POST.get('age')},但没有上传文件")
        elif request.content_type == "application/json":
            prams_data = json.loads(request.body)
            return HttpResponse(f"使用application/json时，姓名：{prams_data.get('name')},年龄：{prams_data.get('age')},token:{request.META.get('HTTP_TOKEN','没有token')}") # 调试信息
        else:
            return HttpResponse(f"使用其他方式时，姓名：{request.POST.get('name')},年龄：{request.POST.get('age')}") # 调试信息



class FileUploadView(View):
    """专门处理文件上传的视图"""
    
    def post(self, request):
        """处理文件上传"""
        if request.FILES:
            uploaded_files = []
            
            # 处理多个文件上传
            for field_name, uploaded_file in request.FILES.items():
                file_info = self.save_file(uploaded_file)
                uploaded_files.append(file_info)
            
            return HttpResponse(f"成功上传 {len(uploaded_files)} 个文件: {uploaded_files}")
        else:
            return HttpResponse("没有上传文件")
    
    def save_file(self, uploaded_file):
        """保存单个文件的方法"""
        import os
        from django.conf import settings
        import uuid
        from datetime import datetime
        
        # 获取文件扩展名
        file_extension = os.path.splitext(uploaded_file.name)[1]
        
        # 生成唯一文件名（避免文件名冲突）
        unique_filename = f"{uuid.uuid4().hex}{file_extension}"
        
        # 按日期创建子目录
        today = datetime.now().strftime('%Y-%m-%d')
        upload_dir = os.path.join(settings.BASE_DIR, 'uploads', today)
        os.makedirs(upload_dir, exist_ok=True)
        
        # 完整的文件路径
        file_path = os.path.join(upload_dir, unique_filename)
        
        # 保存文件
        with open(file_path, "wb") as file:
            for chunk in uploaded_file.chunks():
                file.write(chunk)
        
        return {
            'original_name': uploaded_file.name,
            'saved_name': unique_filename,
            'file_path': file_path,
            'file_size': uploaded_file.size,
            'content_type': uploaded_file.content_type
        }