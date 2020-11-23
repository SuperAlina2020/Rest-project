from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True,null=True)


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,null=True)
