import datetime

from django.utils import timezone

from django.db import models


class Comment(models.Model):
    content = models.TextField()

    def has_article(self):
        return False


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    comments = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)
    date_pub = models.DateField(auto_now=True)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_pub <= now
