from django.contrib import admin
from .models import Question, Option, PersonalityType
# Register your models here.
class OptionInline(admin.TabularInline):
    model = Option
    extra = 2  # Number of empty option forms to display

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(PersonalityType)
