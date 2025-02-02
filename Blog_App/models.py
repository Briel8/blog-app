from django.db import models

class Post(models.Model):
    post_text = models.CharField(max_length=200)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_text
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    commented_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text