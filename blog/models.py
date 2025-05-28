from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    image_name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    content = models.TextField()
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.genera_unique_slug()
        super().save(*args, **kwargs)
    
    def genera_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug
    
    def __str__(self):
        return self.title