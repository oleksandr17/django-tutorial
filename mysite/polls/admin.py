from django.contrib import admin

from .models import Choice, Question


### Simple

# admin.site.register(Question)
# admin.site.register(Choice)


### Customize admin

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#
#
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)


### Create admin field sets

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)


### Add related choices

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # metadata is used for UI representation, check model for details
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # filter panel on right side
    list_filter = ['pub_date']
    # add search field on top
    search_fields = ['question_text', 'pub_date']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)