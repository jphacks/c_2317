from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    TAG_CHOICES = [
        ('programming', 'プログラミング'),
        ('exam', '受験'),
        ('assignment', '課題'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    detail = models.TextField()
    duration = models.IntegerField()  # 日数で管理
    tags = models.CharField(max_length=50, choices=TAG_CHOICES)  # 選択肢で管理


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name