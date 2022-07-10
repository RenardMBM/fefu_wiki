from django.contrib import admin

from article.models import *


class TeacherStoryInline(admin.TabularInline):
    model = StoryTeacher


@admin.register(TeacherRating)
class TeacherRatingAdmin(admin.ModelAdmin):
    inlines = [
        TeacherStoryInline
    ]


admin.site.register(UniversityArticle)
admin.site.register(TeacherArticle)
admin.site.register(StoryTeacher)
