from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date =timezone.now()
        self.save()

    def __str__(self):
        return 'Created:{0} Title:{1}'.format(self.author, self.title)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='documents/', default='defo')
    uploaded_at = models.DateTimeField(auto_now_add=True)