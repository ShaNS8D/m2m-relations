from django.contrib import admin
from .models import Article, Scope, TagPost


class RelationshipInline(admin.TabularInline):
    model = Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

