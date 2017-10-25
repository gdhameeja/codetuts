from django.db import models
from django.db import models
from django.core.urlresolvers import reverse

# Topic class - contains Topic title, slug
class Topic(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()
# Show up in the admin panel
    class Admin:
        pass
# order topics by title
    class Meta:
        ordering = ['title']
# on call all() return title
    def __str__(self):
      return self.title

# get absolute URl for reference
   # def get_absolute_url(self):
       # pass

class Post(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField()
    date = models.DateField()
    topic = models.ForeignKey(Topic)

    class Admin:
        pass
    class Meta:
        pass
    def __str__(self):
        return self.title
    def get_absolute_url(self):
       return reverse("content_urls", kwargs={"slug":self.slug})