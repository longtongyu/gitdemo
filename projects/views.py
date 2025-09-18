import json
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from .models import Projects
from interfaces.models import InterFaces
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .serializers import ProjectSerializers


class ProjectView(View):

    def get(self,request):
        json_data = {
            "code":0,
            "msg":""
        }
        # 查询所有项目
        try:
            qs = Projects.objects.all()
            serializer_obj = ProjectSerializers(instance=qs,many=True)
            return  JsonResponse(serializer_obj.data, safe=False, json_dumps_params={"ensure_ascii": False})
        except Exception:
            json_data["code"] = 1
            json_data["msg"] = "获取项目失败"
            return JsonResponse(json_data,safe=False,json_dumps_params={"ensure_ascii": False})

    def post(self,request):
        request_json = json.loads(request.body.decode("utf-8"))
        # 创建数据
        json_data = {
            "code":0,
            "msg":""
        }
        try:
            
            Projects.objects.create(**request_json)
            json_data["msg"] = "创建成功"
            return JsonResponse(json_data,safe=True,json_dumps_params={"ensure_ascii":False})
        except Exception:
            json_data["code"] = 1
            json_data["msg"] = "项目创建失败"
            return JsonResponse(json_data,safe=True,json_dumps_params={"ensure_ascii":False})        

    


class ProjectDetailView(View):
    

    def get(self,request,pk):
        # 查询单条项目信息
        json_data = {
            "code":0,
            "msg":""
        }
        try:
            obj = Projects.objects.get(pk=pk)
            serializer_obj = ProjectSerializers(instance=obj)
            return JsonResponse( serializer_obj.data,safe=True,json_dumps_params={"ensure_ascii": False})
        except Exception:
            json_data["code"] = 1
            json_data["msg"] = "项目不存在"
            return JsonResponse(json_data,safe=True,json_dumps_params={"ensure_ascii": False})





    def put(self,request,pk):
        # 更新数据
        json_data = {
            "code":0,
            "msg":""

        }
        try:
            request_json = json.loads(request.body.decode("utf-8"))
            obj = Projects.objects.get(pk=pk)
            for field,value in request_json.items():
                setattr(obj,field,value)
            obj.save()
            json_data["msg"] = "数据更新成功"
            serializer = ProjectSerializers(instance=obj)
            return JsonResponse(serializer.data,safe=True,json_dumps_params={"ensure_ascii":False})
        except ObjectDoesNotExist:
            json_data["code"] = 1
            json_data["msg"] = "项目不存在,更新失败"
            return JsonResponse(json_data,safe=True,json_dumps_params={"ensure_ascii":False})



    def delete(self,request,pk):
        # 删除数据
        json_data = {
            "code":0,
            "msg":""
        }
        try:
            obj = Projects.objects.get(pk=pk)
            obj.delete()
            json_data["msg"] = "数据删除成功"
            return JsonResponse(json_data,safe=True,json_dumps_params={"ensure_ascii":False})
        except ObjectDoesNotExist:
            json_data["code"] = 1
            json_data["msg"] = "项目不存在,删除失败"
            return JsonResponse(json_data,safe=True,json_dumps_params={"ensure_ascii":False})






















        # 添加数据
        # Projects.objects.create(name="versa项目",leader="张三",is_execute=True,desc="这是一个versa项目")
        # return HttpResponse(content=f"添加了公有云项目")


        # 批量创建数据
        # projects_list = [
        #     Projects(name="美的项目",leader="张三",is_execute=True,desc="这是一个美的项目"),
        #     Projects(name="普康项目",leader="李四",is_execute=True,desc="这是一个普康项目"),
        #     Projects(name="日本项目",leader="李四",is_execute=True,desc="这是一个日本项目")
        # ]
        
        # Projects.objects.bulk_create(projects_list)

        # return HttpResponse("批量数据创建成功")


        # 更新数据
        # 更新单个对象
        # one_project = Projects.objects.get(pk=1)
        # one_project.desc = "更改一下这个项目描述"
        # one_project.save()
        # return HttpResponse("数据更新成功")

        # 批量更新
        # Projects.objects.update(is_execute=False)
        # return HttpResponse("数据批量更新成功")

        # 更新满足条件的数据
        # 示例：更新 id 大于 1 的项目
        # Projects.objects.filter(id__gt=1).update(is_execute=True)
        # return HttpResponse("条件更新成功")

        # 其他常用的查询示例：
        # 1. 精确匹配
        # Projects.objects.filter(id__exact=1)
        
        # 2. 包含查询（适用于字符串字段）
        # Projects.objects.filter(name__contains="项目")
        
        # 3. 不区分大小写的包含查询
        # Projects.objects.filter(name__icontains="项目")
        
        # 4. 以...开始
        # Projects.objects.filter(name__startswith="美的")
        
        # 5. 以...结束
        # Projects.objects.filter(name__endswith="项目")
        
        # 6. 在列表中
        # Projects.objects.filter(id__in=[1, 2, 3])
        
        # 7. 范围查询
        # Projects.objects.filter(id__range=(1, 5))
        
        # 8. 空值查询
        # Projects.objects.filter(desc__isnull=True)
        
        # 9. 复合条件查询
        # Projects.objects.filter(id__gt=1, is_execute=True)
        
        # 10. 排除查询
        # Projects.objects.exclude(id=1)

        # 查询
        # 获取所有对象
        # all_projects = Projects.objects.all()
        # 遍历对象取字段
        # for p in all_projects:
        #     print(p.id,p.name)

        # 只取某些字段为字典（用于返回给前端）
        # qs = Projects.objects.all().values("id","name")
        # return JsonResponse(list(qs),safe=False,json_dumps_params={"ensure_ascii":False})

        # 只取某个字段列表
        # names = Projects.objects.values_list("name",flat=True)
        # return JsonResponse(list(names),safe=False,json_dumps_params={"ensure_ascii":False})      

        # 获取单个对象
        # one_project = Projects.objects.get(id=1)
        # return JsonResponse(one_project.name,safe=False,json_dumps_params={"ensure_ascii":False})

        # 过滤查询 取第一个对象再取字段

        # obj = Projects.objects.filter(id=1).first()
        # if obj:
        #     return JsonResponse({"id":obj.id,"name":obj.name},json_dumps_params={"ensure_ascii":False})
        # else:
        #     return JsonResponse({"error":"数据不存在"},json_dumps_params={"ensure_ascii":False})

        # 直接取字典
        # obj = Projects.objects.filter(id=1).values("id","name","leader").first()
        # return JsonResponse(obj,safe=False,json_dumps_params={"ensure_ascii":False})

        # 直接使用get
        # obj = Projects.objects.get(id=1)
        # return JsonResponse({"id":obj.id,"name":obj.name},json_dumps_params={"ensure_ascii":False})

        # 多条件查询
        # obj = Projects.objects.filter(is_execute=True,name="美的项目")
        # return JsonResponse(obj.values("id","name").first(),safe=True,json_dumps_params={"ensure_ascii":False}  )

        # 使用q对象进行或查询
        # obj = Projects.objects.filter(Q(id=2)|Q(name="美的项目"))
        # return JsonResponse(list(obj.values("id","name")),safe=False,json_dumps_params={"ensure_ascii":False})


        # 排除查询
        # obj = Projects.objects.exclude(name = "公有云项目")
        # return JsonResponse(list(obj.values("id","name")),safe=False,json_dumps_params={"ensure_ascii":False})

        # 范围查询
        # obj = Projects.objects.filter(id__range=(1,3))
        # return JsonResponse(list(obj.values("id","name")),safe=False,json_dumps_params={"ensure_ascii":False})

        # 包含查询（适用于字符串字段）
        # obj = Projects.objects.filter(name__contains="项目")
        # return JsonResponse(list(obj.values("id","name")),safe=False,json_dumps_params={"ensure_ascii":False})

        # 排序
        # obj = Projects.objects.order_by("id")
        # return JsonResponse(list(obj.values("id","name")),safe=False,json_dumps_params={"ensure_ascii":False})

        # # 降序
        # obj = Projects.objects.order_by("-id")
        # return JsonResponse(list(obj.values("id","name")),safe=False,json_dumps_params={"ensure_ascii":False})

        # 删除数据
        # obj = Projects.objects.get(id=1)
        # obj.delete()
        # return HttpResponse("数据删除成功")

        # 删除满足条件的数据
        # Projects.objects.filter(id__gte=1).delete()
        # return HttpResponse("数据删除成功")

        # 删除所有数据
        # Projects.objects.all().delete()

        # 添加interface 创建所属某个项目的接口 如果主键为id需要传具体id，如果没有指定id传父表对象
        # projects = Projects.objects.get(id=4)
        # InterFaces.objects.create(name="接口4",projects=projects)
        # return HttpResponse("接口添加成功")

        # 关联查询
        # 查询项目id为1的所有接口数据 
        # obj = InterFaces.objects.filter(projects__id=1).values("id","name","projects_id")
        # return JsonResponse(list(obj),safe=False,json_dumps_params={"ensure_ascii":False})


        # 关联查询 反向查询 查询接口id为1的接口所属项目
        # obj = Projects.objects.filter(interfaces__id=1).values("id","name")
        # return JsonResponse(list(obj),safe=False,json_dumps_params={"ensure_ascii":False})