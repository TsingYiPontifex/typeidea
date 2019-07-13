from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DEL = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DEL, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, verbose_name="状态",
                                         default=STATUS_NORMAL)
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DEL = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DEL, '删除'),
    )
    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=STATUS_NORMAL,
                                         verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DEL = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DEL, '删除'),
        (STATUS_DRAFT, '草稿'),
    )
    title = models.CharField(max_length=255, verbose_name="标题")
    desc = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name="内容", help_text="正文必须为mark_down格式")
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=STATUS_NORMAL,
                                         verbose_name="状态")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title
