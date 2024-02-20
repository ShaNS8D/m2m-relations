from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag

class RelationshipInlineFormset(BaseInlineFormSet): 
       
    def clean(self):
        i = 0
        for form in self.forms:
            new_var = 'is_main'
            if form.cleaned_data.get(new_var) == True:
                i += 1
                if i > 1:
                    raise ValidationError('Должен быть только один основной тег')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [RelationshipInline]
    
    


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    

