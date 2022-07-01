from django.contrib import admin

from article.models import *

admin.site.register(UniversityArticle)
admin.site.register(TeacherArticle)
admin.site.register(TeacherRating)
admin.site.register(StoryTeacher)
