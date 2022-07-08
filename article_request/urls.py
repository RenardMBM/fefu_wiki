from django.urls import path

from article_request.views import answer_article_request

urlpatterns = [
    path('api/article_request/<str:article_type>/<int:rid>/answer/',
         answer_article_request),
]
