from django.db import models
from django.urls import reverse

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.TextField(max_length=300)

    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images", default="placeholder.png")

    class Meta:
        abstract = True
        ordering = ['-created']

    def __unicode__(self):
        return u'%s'% self.title

    def get_absolute_url(self):
        return reverse("blog.views.post", args=[self.slug])

class Post(Entry):
    content = models.TextField(max_length=255, default="")

    class Meta(Entry.Meta):
        db_table = 'post_info'

    published = models.BooleanField(default=True)

class Project(Entry):
    github_link = models.CharField(max_length=255, default="")
    implementation_link = models.CharField(max_length=255, default="")

    class Meta(Entry.Meta):
        db_table = 'project_info'

    published = models.BooleanField(default=True)
