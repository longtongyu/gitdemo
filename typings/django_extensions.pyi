from typing import Any, List, Union, Optional
from django.db.models import QuerySet, Model

# Django 字段查找器类型定义
class FieldLookup:
    # 精确匹配
    exact: Any
    iexact: Any
    
    # 包含查询
    contains: Any
    icontains: Any
    
    # 开始/结束匹配
    startswith: Any
    istartswith: Any
    endswith: Any
    iendswith: Any
    
    # 数值比较
    gt: Any  # greater than
    gte: Any  # greater than or equal
    lt: Any  # less than
    lte: Any  # less than or equal
    
    # 列表和范围
    in_: Any  # in list
    range: Any  # range query
    
    # 空值查询
    isnull: Any
    
    # 正则表达式
    regex: Any
    iregex: Any
    
    # 日期时间查询
    year: Any
    month: Any
    day: Any
    hour: Any
    minute: Any
    second: Any
    
    # 外键查询
    pk: Any

# 扩展 QuerySet 类型
class ExtendedQuerySet(QuerySet):
    def filter(self, **kwargs: Any) -> 'ExtendedQuerySet': ...
    def exclude(self, **kwargs: Any) -> 'ExtendedQuerySet': ...
    def update(self, **kwargs: Any) -> int: ...
    def delete(self) -> tuple[int, dict[str, int]]: ... 