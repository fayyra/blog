from django.core.exceptions import PermissionDenied
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField('Picture', upload_to='images/')
    text = models.TextField(max_length=3000)
    data = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.author

    class Meta:
        ordering = ['-data']

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def not_allowed(self):
        raise PermissionDenied


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(max_length=1000)
    data = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', null=True)

    class Meta:
        ordering = ['data']

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    birth = models.DateField(null=True)
    bio = models.TextField(max_length=500, default='')
