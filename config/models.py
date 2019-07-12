from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DEL = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DEL, '删除'),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    href = models.URLField(verbose_name="链接")
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=STATUS_NORMAL,
                                         verbose_name="状态")
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)),
                                         verbose_name="权重", help_text="权重高显示靠前")
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "友链"
        verbose_name_plural = verbose_name


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隐藏'),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
    )
    title = models.CharField(max_length=50, verbose_name='标题')
    display_type = models.PositiveIntegerField(choices=SIDE_TYPE, default=1,
                                               verbose_name="展示类型")
    content = models.CharField(max_length=500, verbose_name="内容", blank=True,
                               help_text="如果不是HTML，可为空")
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=STATUS_SHOW,
                                         verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="作者")
    crated_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "侧边栏"
        verbose_name_plural = verbose_name

