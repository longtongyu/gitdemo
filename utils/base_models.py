
from django.db import models


class BaseModel(models.Model):
    
    id = models.IntegerField(primary_key=True,verbose_name="主键",help_text="自增主键id")
    create_time = models.TimeField(verbose_name="创建时间",auto_now_add=True)
    update_time = models.TimeField(verbose_name="修改时间",auto_now=True)


    class Meta:
        abstract = True