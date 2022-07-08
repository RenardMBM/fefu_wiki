from django.contrib import admin

from article.models import *


class TeacherStoryInline(admin.TabularInline):
    model = StoryTeacher


class TeacherRatingAdmin(admin.ModelAdmin):
    inlines = [
        TeacherStoryInline
    ]


admin.site.register(UniversityArticle)
admin.site.register(TeacherArticle)
admin.site.register(TeacherRating, TeacherRatingAdmin)
admin.site.register(StoryTeacher)

