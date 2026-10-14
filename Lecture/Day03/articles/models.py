from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # python의 매직 메서드 (print할 때 보여지는 문자열을 정의할 수 있는 메서드)
    def __str__(self):
        return f'{self.id}번 글: {self.title} ({self.author})'