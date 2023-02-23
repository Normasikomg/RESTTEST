from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts',
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(default=True)
    owner = models.ForeignKey('auth.User', related_name='comments',
                              on_delete=models.CASCADE)
    VOTE_TYPE = (
        ('Done', 'Решен'),
        ('Not done', 'Не решен'),
        ('Freezed', 'Заморожен')
    )
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    review = models.CharField(max_length=20, choices=VOTE_TYPE, default=open)
    

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.review



