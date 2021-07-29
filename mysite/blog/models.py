from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # models.ForeignKey - 다른 모델에 대한 링크를 의미합니다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # CharField : 글자수가 제한된 텍스트를 정의할 때 사용
    title = models.CharField(max_length=200)
    # TextField : 글자수에 제한없는 텍스트 정의
    text = models.TextField()
    # models.DateTimeField - 날짜와 시간을 의미합니다.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
