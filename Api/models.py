from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_posted"]
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
