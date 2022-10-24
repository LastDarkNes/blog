from django.db import models
from  django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=64, verbose_name='name')


class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=30, verbose_name='title')
    description = models.TextField(null=True, verbose_name='description')
    image = models.ImageField(upload_to='', null=True, blank=True, verbose_name='image')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='category', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('single_post', args=[str(self.pk)])

    def get_comments(self):
        return Comment.objects.filter(post=self)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='author')
    text = models.CharField(max_length=70, verbose_name='text')
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='post')
