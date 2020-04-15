from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    category_choices = (
        ('News','News'),
        ('Technology','Technology'),
        ('Sports','Sports'),
        ('Lifestyle','Lifestyle'),
    )
    cover = models.FileField(default='')
    cover_2 = models.FileField(default='')
    author = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=2000, default='')
    slug = models.SlugField(default='')
    text_2 = models.TextField(default='')
    l_heading = models.CharField(max_length=2000, default='')
    l_heading_text = models.CharField(max_length=2000, default='')
    quote = models.CharField(max_length=2000, default='')
    quotes_name = models.CharField(max_length=2000, default='')
    s_heading = models.CharField(max_length=2000, default='')
    s_heading_text = models.CharField(max_length=2000, default='')
    category = models.CharField(max_length=2000, choices=category_choices, default='')
    created_date = models.DateTimeField(default='')
    text = models.TextField(default='')
    tag_1 = models.CharField(max_length=2000, default='')
    tag_2 = models.CharField(max_length=2000, default='')
    tag_3 = models.CharField(max_length=2000, default='')
    tag_4 = models.CharField(max_length=2000, default='')

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title