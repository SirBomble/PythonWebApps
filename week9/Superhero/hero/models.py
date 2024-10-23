from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    strength = models.CharField(max_length=100, default='')
    weakness = models.CharField(max_length=100, default='')
    image = models.CharField(max_length=100, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='superheroes')
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('blog_list')


class Article(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.blog.title} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('article_list')
