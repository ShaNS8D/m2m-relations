from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class TagPost(models.Model):
    name = models.CharField(max_length=125, verbose_name='Раздел')
    tagposts = models.ManyToManyField(Article, related_name='scopes', through='Scope')

    def __str__(self):
        return self.name
    

class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    tag = models.ForeignKey(TagPost, on_delete = models.CASCADE)
    is_main = models.BooleanField()
    