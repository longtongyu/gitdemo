from django.db import models
from projects.models import Projects

# 通用的字段 可以放到basemodel中
from utils.base_models import BaseModel
 
# Create your models here.

class InterFaces(BaseModel):
    # id = models.IntegerField(primary_key=True,verbose_name="主键",help_text="自增主键id")
    name = models.CharField(max_length=50, verbose_name="接口名称")
    # 父表数据删除，子表也删除
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name="所属项目id", help_text="外键id")
    # 父表数据删除，抛出异常
    # projects = models.ForeignKey(Projects, on_delete=models.PROTECT, verbose_name="所属项目id", help_text="外键id")
    # 父表数据删除，对应的字段的数据设为null
    # projects = models.ForeignKey(Projects, on_delete=models.SET_NULL, null=True, verbose_name="所属项目id", help_text="外键id")
    # create_time = models.TimeField(verbose_name="创建时间",auto_now_add=True)
    # update_time = models.TimeField(verbose_name="修改时间",auto_now=True)

    class Meta:
        db_table = "tb_interfaces"
        verbose_name = "接口表"
        verbose_name_plural = "接口表"
        ordering = ['id']