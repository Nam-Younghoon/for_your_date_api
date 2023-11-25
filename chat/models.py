from django.db import models
from django.conf import settings

class Chat(models.Model):
    title = models.CharField('제목', max_length=150)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime = models.CharField("데이트시간", max_length=150)
    question = models.TextField("질문")
    answer = models.TextField("답변")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
