from django.db import models
from blog.models import Post


# Create your models here.

class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DEL = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DEL, '删除'),
    )
    target = models.ForeignKey(Post,on_delete=models.CASCADE, verbose_name="评论目标")
    content = models.CharField(max_length=2000, verbose_name="评论内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=STATUS_NORMAL,
                                         verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
