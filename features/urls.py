from django.urls import path

from features.views import answer_question, news_list

app_name = 'features'
urlpatterns = [
    path('question-answers/', answer_question, name='answer_question'),
    path('news_list/', news_list, name='news_list')
]
