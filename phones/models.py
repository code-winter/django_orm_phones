from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50, default='Phone')
    price = models.IntegerField(default=0)
    image = models.URLField(max_length=150, default=None)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(default=0)
    slug = models.SlugField(max_length=100, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
