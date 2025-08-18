from tabnanny import verbose
from django.db import models

# Create your models here.
# 1.创建数据表Peple 
# 2.创建用户名、年龄、性别字段

class Peple(models.Model):
    # 对应数据库中的varchar
    username = models.CharField(max_length=20)
    # int类型
    age = models.IntegerField()
    # bool类型
    gender = models.BooleanField(default=True)




class projects(models.Model):
    # 主键
    id  = models.IntegerField(primary_key=True,verbose_name="主键",help_text="项目id为主键")
    name = models.CharField(max_length=50,verbose_name="项目名称",help_text="项目名称",unique=True)
    leader = models.CharField(max_length=50,verbose_name="项目负责人",help_text="项目负责人",null=True)
    is_execute = models.BooleanField(verbose_name='是否启动项目',help_text="1:启动 2:暂停",default=True)
    desc = models.TextField(verbose_name="项目描述",help_text="请输入项目描述",null=True,blank=True)
    # auto_now_add 创建项目的时间 只会更新一次
    create_time = models.TimeField(verbose_name="项目创建时间",auto_now_add=True)
    # auto_now 每次更新都会更新
    update_time = models.TimeField(verbose_name="修改时间",auto_now=True)

    class Meta:
        db_table = 'tb_project'
        verbose_name = "项目表"
        ordering = ['id']
        
