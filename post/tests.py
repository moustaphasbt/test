import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Article


class ArticleModelTest(TestCase):

    def test_was_published_recently_with_old_article(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_article = Article(pub_date=time)
        self.assertIs(old_article.was_published_recently(), False)

    def test_was_published_recently_with_future_article(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_article = Article(date_pub=time)
        self.assertIs(future_article.was_published_recently(), False)
