from django.contrib import admin

# Register your models here.
from prepa.models import Option, Question

class OptionInline(admin.TabularInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

    

admin.site.register(Question,QuestionAdmin)